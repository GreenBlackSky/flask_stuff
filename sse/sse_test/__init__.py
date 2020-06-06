from flask import Flask, render_template
from flask_sse import sse


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    with app.app_context():
        from . import routes
        app.register_blueprint(sse, url_prefix='/stream')

    return app
