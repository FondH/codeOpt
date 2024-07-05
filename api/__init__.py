
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

from api.models import Detection, ThreadTask
from views.task import process_code
import threading, time


def poll_pending_tasks(app):
    #
    while True:
        try:
            with app.app_context():
                # 查询状态为 pending 的任务
                pending_tasks = ThreadTask.query.filter_by(status='Pending').all()
                for task in pending_tasks:
                    print(f"search a pending work(task_id:{task.task_id}")
                    #task.status = 'Working'
                    #db.session.commit()
                    detection = Detection.query.filter_by(id=task.detection_id).first()
                    file_path = task.file_path

                    task_info = {
                        'task_id': task.task_id,
                        'detectModules': detection.detect_modules,
                        'codeLanguage': detection.code_language,
                        'useLargeModel': detection.use_large_model,
                        'prompt': detection.prompt,
                        'model': detection.model
                    }
                    #print(task_info)
                    threading.Thread(target=process_code, args=(task_info, file_path,app)).start()
        except Exception as e:
            print(f"Error polling tasks: {e}")
        time.sleep(10)
def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    CORS(app)
    db.init_app(app)
    jwt.init_app(app)


    with app.app_context():

        from views.auth import auth_blueprint
        from views.admin import admin_blueprint
        from views.task import task_blueprint
        from views.overview import overview_blueprint

        app.register_blueprint(auth_blueprint)
        app.register_blueprint(admin_blueprint)
        app.register_blueprint(task_blueprint)
        app.register_blueprint(overview_blueprint)

        db.create_all()

    threading.Thread(target=poll_pending_tasks,args=(app,)).start()

    return app


app = create_app()
