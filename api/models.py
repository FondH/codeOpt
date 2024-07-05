from api import db
from datetime import datetime
import hashlib

def _hash(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()
class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rank = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(64), nullable=False)
    api_key = db.Column(db.String(128), nullable=True)
    password = db.Column(db.String(128), nullable=False)
    plain_pass = db.Column(db.String(20), nullable=True)
    is_active = db.Column(db.Boolean, default=1)

    def hash_password(self, password):
        self.password = _hash(password)

    def verify_password(self, password):
        print(self.password, " ", _hash(password))
        return _hash(password) == self.password
class Detection(db.Model):
    __tablename__ = 'detection'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    detection_id = db.Column(db.String(36), unique=True, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    file_path = db.Column(db.String(255))
    upload_method = db.Column(db.String(10)) # file or github
    submitter_name = db.Column(db.String(50))
    submit_time = db.Column(db.String(50))
    file_name = db.Column(db.String(255))
    file_size = db.Column(db.Integer)
    code_language = db.Column(db.String(20))
    detect_strength = db.Column(db.String(20))
    detect_modules = db.Column(db.String(255))  # JSON string
    use_large_model = db.Column(db.Boolean, default=False)
    model = db.Column(db.String(50))
    prompt = db.Column(db.String(255))

    result = db.Column(db.Text) # 存储结果
    result_path = db.Column(db.String(255), default='None')


class ThreadTask(db.Model):
    __tablename__ = 'threadingTask'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_id = db.Column(db.String(36), unique=True, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    detection_id = db.Column(db.String(36), db.ForeignKey('detection.detection_id'), nullable=False)
    progress = db.Column(db.Integer, default=0)
    status = db.Column(db.String(20), default='Pending')
    start_time = db.Column(db.String(50))
    end_time = db.Column(db.String(50))

    file_path = db.Column(db.String(255))
    is_canceled = db.Column(db.Boolean, default=False)


