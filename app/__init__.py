from flask import Flask, render_template
from config import config
from flask_pymongo import PyMongo

mongo = PyMongo()
#instentiate extensions

def create_app(config_name):
    app = Flask(__name__, static_url_path='')
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #init_app for extensions
    mongo.init_app(app)

    from .main import main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app