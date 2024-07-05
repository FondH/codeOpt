import os
from datetime import timedelta
class Config:
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
