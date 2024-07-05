import json
from uuid import uuid4
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from api.models import Detection, db, ThreadTask
from sqlalchemy import func
from datetime import datetime, timedelta
overview_blueprint = Blueprint('overview', __name__)

@overview_blueprint.route('/api/submit_overview', methods=['GET'])
@jwt_required()
def submit_overview():
    user_id = get_jwt_identity()
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=7)

    # 格式化日期为字符串
    start_date_str = start_date.strftime("%Y/%m/%d %H:%M:%S")
    end_date_str = end_date.strftime("%Y/%m/%d %H:%M:%S")

    submissions = Detection.query.filter(
        Detection.user_id == user_id,
    ).all()
    #print(submissions.__len__())
    date_counts = {}
    for submission in submissions:
        submit_time = datetime.strptime(submission.submit_time, "%Y/%m/%d %H:%M:%S")
        date_str = submit_time.strftime("%m-%d")
       #print(date_str)
        if date_str in date_counts:
            date_counts[date_str] += 1
        else:
            date_counts[date_str] = 1

    labels = []
    data = []
    for i in range(8):
        date = start_date + timedelta(days=i)
        date_str = date.strftime("%m-%d")
        labels.append(date_str)
        data.append(date_counts.get(date_str, 0))

    total_submissions = len(submissions)
    #print(data)
    #print(labels)

    return jsonify({
        'labels': labels,
        'data': data,
        'total_submissions': total_submissions
    })


@overview_blueprint.route('/api/submit_recent', methods=['GET'])
@jwt_required()
def recent_submissions():
    # 获取最近15天的提交记录
    user_id = get_jwt_identity()
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=15)

    start_date_str = start_date.strftime("%Y/%m/%d %H:%M:%S")
    end_date_str = end_date.strftime("%Y/%m/%d %H:%M:%S")

    # 添加连接条件
    submissions = ThreadTask.query.filter(
        ThreadTask.user_id == user_id,
        func.strftime('%Y/%m/%d %H:%M:%S', ThreadTask.start_time) >= start_date_str,
    ).all()


    submission_list = []
    for submission in submissions:
        det = Detection.query.filter(
                Detection.id == submission.detection_id,
            ).first()
        submission_list.append({
            'task_id':submission.task_id,
            'submitter': det.submitter_name,
            'fileName': det.file_name,
            'submitTime': det.submit_time,
            'status': submission.status
        })

    if submission_list.__len__() > 0:
        #print("dd",submission_list)
        return jsonify({'submissions': submission_list[submission_list.__len__()-10:]}), 200
    else:
        return jsonify({'msg': 'completely empty' }), 406


@overview_blueprint.route('/api/view-report/<task_id>', methods=['GET'])
@jwt_required()
def view_report(task_id):
    try:
        task = ThreadTask.query.filter_by(task_id=task_id).first()
        detection = Detection.query.filter_by(id=task.detection_id).first()

        return jsonify({'msg':'get report','res':json.loads(detection.result)}), 200

    except Exception as e:
        print(f'Except: view-report {e}')
        return jsonify({
            'msg':'no task',
        }), 406
