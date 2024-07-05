import json
from uuid import uuid4
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from api.models import Detection, db, ThreadTask
import os
import time
from api.detect import detect
from flask import current_app
task_blueprint = Blueprint('task', __name__)
file_dir = os.path.join(os.getcwd(), 'files') 


@task_blueprint.route('/api/submit-code', methods=['POST'])
def submit_code():
    detection_id = str(uuid4())
    user_id = request.form.get('user_id')

    file = request.files.get('file')
    if file:
        file_name = file.filename
        file_pt = os.path.join(file_dir, file_name)

        file.save(file_pt)  # 保存文件到指定路径
        file_size = os.path.getsize(file_pt)
        # commit a detection
        detection = Detection(
            detection_id=detection_id,
            user_id=user_id,
            upload_method=request.form.get('uploadMethod'),
            submitter_name=request.form.get('submitterName'),
            submit_time=request.form.get('submitTime'),
            file_name=request.form.get('fileName'),
            file_size=request.form.get('fileSize'),
            code_language=request.form.get('codeLanguage'),
            detect_strength=request.form.get('detectStrength'),
            detect_modules=request.form.get('detectModules'),
            use_large_model=request.form.get('useLargeModel') == 'true',
            model=request.form.get('model'),
            prompt=request.form.get('prompt'),
            file_path=file_pt,
            result="None",
        )
        db.session.add(detection)
        db.session.commit()

        algorithmSettings = json.loads(request.form.get('algorithmSettings'))
        modelSettings =  json.loads(request.form.get('modelSettings'))
        # print(algorithmSettings)
        # print(modelSettings)

        ## commit a task, a task may be multi detections
        task_id = str(uuid4())
        # debug info
        task_info = {
            'task_id':task_id,
            'status': 'Pending',
            'user_id': user_id,
            'file': request.form.get('file'),
            'uploadMethod': request.form.get('uploadMethod'),  # file or github
            'submitterName': request.form.get('submitterName'),
            'submitTime': request.form.get('submitTime'),
            'fileName': request.form.get('fileName'),
            'codeLanguage': request.form.get('codeLanguage'),
            'detectStrength': request.form.get('detectStrength'),
            'detectModules': request.form.get('detectModules'),  # Ensure this is a string from JSON
            'useLargeModel': request.form.get('useLargeModel'),
            'model': request.form.get('model'),
            'prompt': request.form.get('prompt'),
            'progress': 0
        }
        print(task_info)
        thread_task = ThreadTask(
            status='Pending',
            task_id=task_id,
            detection_id=detection.id,
            user_id=user_id,
            start_time=time.strftime("%Y-%m-%d %H:%M:%S"),
            file_path = file_pt,
        )
        db.session.add(thread_task)
        db.session.commit()

        #threading.Thread(target=process_code, args=(task_info, file_pt, current_app)).start()
        return jsonify({'status':0,'msg':'task created successfully', 'task_id': task_id})

    else:
        return jsonify({'status':1,'msg':'task created unsuccessfully', 'task_id': -1})


def process_code(task_info, file_path, app):

    with app.app_context():
        detect_moudles = task_info['useLargeModel']
        print("QQFASQ",detect_moudles)
        # rs json.dumps({  'file_name': os.path.basename(file_path),
        #             'standard_check_res':cpp_standard_check(file_path),
        #             'syntax_check_res':cpp_syntax_analysis(file_path)}
        try:

            if task_info['useLargeModel']:
                pass
            # 更新数据库中的进度
            task = ThreadTask.query.filter_by(task_id=task_info['task_id']).first()
            task.progress = 50
            task.status = 'Working'
            db.session.commit()
            # 根据 detection_id 查询 Detection 表，并更新 result 字段
            detection = Detection.query.filter_by(id=task.detection_id).first()
            if detection:
                file_pt = detection.file_path.replace('\\', '\\\\')
                #print(file_pt)
                code_language = file_path.split('.')[-1].lower()
                if code_language in ['c', 'cpp', 'java', 'python']:
                    rs = detect(file_pt,code_language, detectModules=detect_moudles)
                    detection.result = json.dumps(rs)
                    db.session.commit()
                    #print(f"detection refrash with {rs}")
                task.progress = 100
                task.status = 'Done'
                db.session.commit()
                print("ThreadTask refrash")

        except Exception as e:
            task.progress = 0
            task.status = 'Pending'
            print(f"process code Exception {e}")


@task_blueprint.route('/api/task-status/<task_id>', methods=['GET'])
def task_status(task_id):
    task = ThreadTask.query.filter_by(task_id=task_id)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify({
        'task_id': task.task_id,
        'detection_id': task.detection_id,
        'progress': task.progress,
        'status': task.status,
    })


@task_blueprint.route('/api/tasks/<task_id>/cancel', methods=['POST'])
def cancel_task(task_id):
    # for task in tasks:
    #     if task['id'] == task_id:
    #         task['status'] = 'canceled'
    #         task['progress'] = 0
    #         break
    return jsonify({'message': 'Task canceled'})

@task_blueprint.route('/api/tasks/<task_id>/details', methods=['GET'])
def task_details(task_id):
    thread_task = ThreadTask.query.filter_by(task_id=task_id).first()
    if thread_task:
        detection = Detection.query.filter_by(id=thread_task.detection_id).first()
        if detection:
            return jsonify({
                'task_id': task_id,
                'detection_id': detection.detection_id,
                'progress': thread_task.progress,
                'status': thread_task.status,
                'submit_time': detection.submit_time,
                'file_name': detection.file_name,
                'use_large_model': detection.use_large_model,
                'model': detection.model,
                'prompt': detection.prompt
            })
    return jsonify({'message': 'Task not found'})


@task_blueprint.route('/api/task_table', methods=['GET'])
@jwt_required()
def task_results():
    user_id = get_jwt_identity()
    tasks = ThreadTask.query.filter_by(user_id=user_id).all()
    results = []

    for task in tasks:
        detection = Detection.query.filter_by(id=task.detection_id).first()
        results.append({
            'task_id': task.task_id,
            'detection_id': task.detection_id,
            'progress': task.progress,
            'status': task.status,
            'submit_time': detection.submit_time,
            'file_name': detection.file_name,
            'use_large_model': detection.use_large_model,
            'model': detection.model,
            'prompt': detection.prompt
        })

    return jsonify({'status': '0', 'results': results})



@task_blueprint.route('/api/available-models', methods=['GET'])
def available_models():
    models = ['Model A', 'Model B', 'Model C']
    return jsonify({'models': models})