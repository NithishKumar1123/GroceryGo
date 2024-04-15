import os
current_directory = os.path.abspath(os.path.dirname(__file__))

class Config():
    SQLITE_DB_DIR = os.path.join(current_directory, '../db_directory')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(SQLITE_DB_DIR, 'MarketMateDB.sqlite3')
    SECRET_KEY = 'hdyg47f8fnsyvbs'
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_PASSWORD_SALT = 'defefygrs678bfr4'
    SECURITY_CHANGEABLE = True
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_UNAUTHORIZED_VIEW = None
    WTF_CSRF_ENABLED = False
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authentication-Token'
    # CELERY_BROKER_URL = "redis://localhost:6379/1"
    # CELERY_RESULT_BACKEND = "redis://localhost:6379/2"
    # CELERY_TIMEZONE = "Asia/Kolkata"
    # CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
    # REDIS_URL = "redis://localhost:6379"
    DEBUG = True