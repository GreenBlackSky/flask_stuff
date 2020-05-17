from flask import Flask
from flask_assets import Environment
from .assets import pack_js


assets = Environment()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    assets.init_app(app)

    with app.app_context():
        from .import routes
        pack_js(assets)

    return app
