from flask import Flask 

from .main import main

def create_app(config_object='pymongoexample.settings'):
    app = Flask(__name__,template_folder='../templates')
    app.secret_key = 'mysecret'

    app.config.from_object(config_object)

    app.register_blueprint(main)

    return app