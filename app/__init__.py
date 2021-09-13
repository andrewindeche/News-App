from flask import Flask
from .config import DevConfig
from flask_sqlalchemy import SQLAlchemy

def create_app(config_name):

    app = Flask(__name__,instance_relative_config = True)

    app.config.from_object(DevConfig)
    app.config.from_pyfile('config.py')


     # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    return app
