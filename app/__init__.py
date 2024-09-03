from flask import Flask
from flask_wtf.csrf import CSRFProtect
from config import Config
import os
from os import environ


def create_app(appConfig=Config):
    app = Flask(__name__, static_folder="./templates", static_url_path="/")
    app.config.from_object(appConfig)


    @app.route('/')
    def index():
        return app.send_static_file('index.html')


    return app