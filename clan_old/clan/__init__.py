"""Initialize module."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


from .auth import bp as auth_bp
# from .tree import bp as tree_bp
from .documents import bp as docs_bp
# from .calendar import bp as calendar_bp

def create_app() -> Flask:
    """Create new app."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        app.register_blueprint(auth_bp)
        app.register_blueprint(docs_bp)
        app.add_url_rule('/', endpoint='index')
        db.create_all()

    return app
