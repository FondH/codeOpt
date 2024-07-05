import os
from datetime import timedelta
class Config:
    # 启动配置
    HOST = '0.0.0.0'
    PORT = 10262
    DEBUG = True

    SECRET_KEY = 'dd2214124'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///CodeOpt2.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # jwt
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-xxx'
    JWT_COOKIE_CSRF_PROTECT = True
    JWT_CSRF_CHECK_FORM = True
    JWT_ACCESS_TOKEN_EXPIRES = os.environ.get('JWT_ACCESS_TOKEN_EXPIRES') or timedelta(days=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    PROPAGATE_EXCEPTIONS = True

    # LLm
    remot_url = 'http://localhost:11434'
    os.environ['http_proxy'] = ''
    os.environ['https_proxy'] = ''


    # 启用 Mysql
    USE_MYSQL = False
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'your_password'
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = '3306'
    MYSQL_DB = 'CodeOpt2'

    # 根据 USE_MYSQL 选择数据库
    if USE_MYSQL:
        SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}'
    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///CodeOpt2.db'