from flask import Flask

def create_flask_app(blueprints):
    application = Flask(__name__)
    return application
