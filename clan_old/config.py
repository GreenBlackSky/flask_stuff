
class Config:
    _connection_data = {
        'type': 'postgresql+psycopg2',
        'user': 'john',
        'password': 'qwerty',
        'host': 'localhost',
        'port': '5432',
        'database': 'test'
    }

    SECRET_KEY = 'dev'
    FLASK_ENV = 'development'
    FLASK_APP = 'clan'
    FLASK_DEBUG = 1

    SQLALCHEMY_DATABASE_URI = "{type}://{user}:{password}@{host}:{port}/{database}".format(**_connection_data)
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False