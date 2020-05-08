from flask import Flask
from flask_assets import Environment
from .assets import compile_assets


assets = Environment()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    assets.init_app(app)

    with app.app_context():
        from .admin import admin_routes
        from .main import main_routes

        app.register_blueprint(admin_routes.admin_bp)
        app.register_blueprint(main_routes.main_bp)
        compile_assets(assets)

        return app
