from flask import Flask
from back_end.server.routes import register_routes


app = Flask(__name__)

register_routes(app)
