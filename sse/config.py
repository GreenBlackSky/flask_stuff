import redis

class Config:

    _config = {
        'password': 'qwerty',
        'host_url': 'localhost',
        'port': '5001'
    }
    redis_connection_line = "redis://:{password}@{host_url}:{port}".format(**_config)
    REDIS_URL = redis_connection_line

    SECRET_KEY = 'dev'
    FLASK_ENV = 'development'
    FLASK_APP = 'auth'
    FLASK_DEBUG = 1

    TEMPLATES_FOLDER = 'templates'
