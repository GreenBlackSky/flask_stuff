from datetime import datetime

from . import db


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)


class Document(db.Model):
    __tablename__ = 'documents'

    doc_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.Text, nullable=False)
