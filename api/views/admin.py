from flask import Blueprint, render_template
from api.models import User, Detection, ThreadTask

from api.views.task import process_code

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return render_template('users.html', users=users)

@admin_blueprint.route('/getdetections', methods=['GET'])
def get_detections():
    detections = Detection.query.all()
    return render_template('detections.html', detections=detections)


@admin_blueprint.route('/gettasks', methods=['GET'])
def get_tasks():
    tasks = ThreadTask.query.all()
    return render_template('tasks.html', tasks=tasks)

@admin_blueprint.route('/proc/<task_id>', methods=['GET'])
def proc(id):

    from flask import current_app
    process_code(id,'',current_app)

@admin_blueprint.route('/test_erupt', methods=['GET'])
def test_erupt_simultaneous():
    from api import db
    import random

    tasks = ThreadTask.query.all()
    ids = []
    if len(tasks) >= 4:
        tasks_to_update = random.sample(tasks, 4)
        for task in tasks_to_update:
            task.status = "Pending"
            ids.append(task.task_id)

        db.session.commit()
        print("frash 4 task to be Pending")
        print(f'task_id:{ids}')