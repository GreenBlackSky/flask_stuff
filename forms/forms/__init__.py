import os
from flask import Flask


def create_app():
    app = Flask(
        __name__,
        instance_relative_config=False,
        template_folder='templates'
    )

    app.config['SECRET_KEY'] = os.urandom(32)
    app.config['RECAPTCHA_PUBLIC_KEY'] = 'qwerty'
    app.config['RECAPTCHA_PARAMETERS'] = {'size': '100%'}

    with app.app_context():
        from . import routes

    return app
