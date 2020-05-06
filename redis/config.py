import redis

class Config:


    _config = {
        'password': 'qwerty',
        'host_url': 'localhost',
        'port': '5001'
    }
    redis_connection_line = "redis://:{password}@{host_url}:{port}".format(**_config)

    SECRET_KEY = 'dev'
    FLASK_ENV = 'development'
    FLASK_APP = 'auth'
    FLASK_DEBUG = 1

    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.from_url(redis_connection_line)

    TEMPLATES_FOLDER = 'templates'
