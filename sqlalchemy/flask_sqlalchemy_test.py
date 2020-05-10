from flask import Flask
from flask_sqlalchemy import SQLAlchemy


connection_data = {
    'type': 'postgresql+psycopg2',
    'user': 'john',
    'password': 'qwerty',
    'host': 'localhost',
    'port': '5432',
    'database': 'test'
}
DB_URL = "{type}://{user}:{password}@{host}:{port}/{database}".format(**connection_data)


db = SQLAlchemy()
class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    with app.app_context():
        db.create_all()
        jon = User('Jon', 'Odin')
        db.session.add(jon)
        db.session.commit()

    @app.route('/')
    def hello():
        return "Hello, world"

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0')
