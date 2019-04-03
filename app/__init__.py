from flask import Flask
from config import app_config
from .routing import register_routes


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    register_routes(app)

    # Logging handler
    # DB initialise and handler

    return app
