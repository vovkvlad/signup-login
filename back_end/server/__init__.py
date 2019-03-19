from flask import Flask
from server.routes import register_routes
from server.db import db

def create_app(test_config=None):
    app = Flask(__name__)
    print("==========================FLASK ROOT_PATH======================")
    print(app.root_path)
    print("==========================FLASK ROOT_PATH======================")
    with app.app_context():
        db.init_app(app)

    register_routes(app)
    return app
