from flask import Blueprint, render_template
from api.models import User, Detection, ThreadTask
from api.views.task import process_code

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/getusers', methods=['GET'])
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