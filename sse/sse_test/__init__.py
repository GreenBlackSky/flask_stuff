from flask import Flask, render_template
from flask_assets import Environment
from flask_sse import sse

from .assets import compile_assets


assets = Environment()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    assets.init_app(app)

    with app.app_context():
        from . import routes
        compile_assets(assets)
        app.register_blueprint(sse, url_prefix='/stream')

    return app
