import redis

class Config:

    SECRET_KEY = 'dev'
    FLASK_ENV = 'development'
    FLASK_APP = 'auth'
    FLASK_DEBUG = 1

    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.from_url('127.0.0.1:5001')

    TEMPLATES_FOLDER = 'templates'
