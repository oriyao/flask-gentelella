from flask import Flask, url_for
from flask_login import LoginManager
from importlib import import_module
import logging
from logging.handlers import RotatingFileHandler

from os import path
import os
from app.setting import config
from app.mydb import initial_mongodb

from flask_pymongo import PyMongo

mongo = PyMongo()

login_manager = LoginManager()

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')
    app = Flask(__name__, static_folder='base/static')
    app.config.from_object(config[config_name])
    # app.logger.warning(app.config["MONGO_URI"] )
    app.config["MONGO_URI"] = "mongodb://testuser:testpassword@152.32.132.155:27017/test20210102?authSource=admin"
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)


    # command function
    register_cmd(app)

    configure_logs(app)
    # Print initial logs
    app.logger.info('oriyao-flask-blog initial')
    apply_themes(app)
    app.logger.info('config_name:' + str(config_name))
    app.logger.info('config_name:' + str(config[config_name]))
    app.logger.info(app.config["TESTENV"])
    return app


def configure_logs(app):
    app.logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = RotatingFileHandler('logs/oriyao-flask-gentelella.log', maxBytes=1000 * 1024, backupCount=10)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(file_handler)


def register_extensions(app):
    login_manager.init_app(app)
    mongo.init_app(app)


def register_blueprints(app):
    for module_name in ('base', 'forms', 'ui', 'home', 'tables', 'data', 'additional', 'base'):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def configure_database(app):
    pass


def apply_themes(app):
    @app.context_processor
    def override_url_for():
        return dict(url_for=_generate_url_for_theme)

    def _generate_url_for_theme(endpoint, **values):
        if endpoint.endswith('static'):
            themename = values.get('theme', None) or \
                app.config.get('DEFAULT_THEME', None)
            if themename:
                theme_file = "{}/{}".format(themename, values.get('filename', ''))
                if path.isfile(path.join(app.static_folder, theme_file)):
                    values['filename'] = theme_file
        return url_for(endpoint, **values)

def register_cmd(app):
    @app.cli.command()
    def initdb():
        """Initialize the database."""
        initial_mongodb()


