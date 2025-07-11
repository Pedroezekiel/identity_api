# app/__init__.py

from flask import Flask
from flask_jwt_extended import JWTManager
from app.db import db
from config.config import Config
from dotenv import load_dotenv
from app.routes.auth_routes import auth_bp
import os

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    JWTManager(app)

    # Import models to register them
    with app.app_context():
        db.create_all()

    app.register_blueprint(auth_bp)
    return app
