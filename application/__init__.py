from flask import Flask
from application.apis import api

def create_app():
    app = Flask(__name__)
    api.init_app(app)
    return app

