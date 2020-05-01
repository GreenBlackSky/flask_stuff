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


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


db.create_all()


jon = User('Jon', 'Odin')


db.session.add(jon)
db.session.commit()


@app.route('/')
def hello():
    return "Hello, world"

