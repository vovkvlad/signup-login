from flask import Flask
from server.routes import register_routes


def create_app(test_config=None):
    app = Flask(__name__)
    print("==========================FLASK ROOT_PATH======================")
    print(app.root_path)
    print("==========================FLASK ROOT_PATH======================")
    register_routes(app)
    return app
