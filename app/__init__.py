# app/__init__.py

from flask import Flask
from flask_jwt_extended import JWTManager
from app.db import db
from config.config import Config
from dotenv import load_dotenv
from app.routes.auth_routes import auth_bp
from app.routes.organization_routes import organization_bp
from app.routes.role_routes import role_bp
from app.routes.user_org_role_routes import user_org_role_bp
from app.routes.invitation_routes import invitation_bp
from app.services.role_service import RoleService
from app.repositories.role_repository import RoleRepository
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
        # Seed predefined roles
        RoleService(RoleRepository()).seed_predefined_roles()

    app.register_blueprint(auth_bp)
    app.register_blueprint(organization_bp)
    app.register_blueprint(role_bp)
    app.register_blueprint(user_org_role_bp)
    app.register_blueprint(invitation_bp)
    return app
