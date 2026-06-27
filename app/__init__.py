from flask import Flask

from app.routes.auth import auth
from app.routes.student import student


def create_app():

    app = Flask(__name__)

    app.config["SECRET_KEY"] = "project_sentinel_secret_key"

    app.register_blueprint(auth)
    app.register_blueprint(student)

    return app