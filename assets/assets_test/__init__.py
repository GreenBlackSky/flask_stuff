from flask import Flask
from flask_assets import Environment, Bundle


assets = Environment()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    assets.init_app(app)

    with app.app_context():
        from . import routes
        app.register_blueprint(routes.bp)

        return app
