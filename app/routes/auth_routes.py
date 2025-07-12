from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app import db
from app.services.user_org_role_service import UserOrgRoleService
from app.repositories.user_org_role_repository import UserOrganizationRoleRepository
from app.models.role import Role

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

user_repo = UserRepository()
user_service = UserService(user_repo)
user_org_role_service = UserOrgRoleService(UserOrganizationRoleRepository())


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    try:
        user = user_service.register_user(email, password)
        return jsonify({'message': 'User created', 'user': {'id': user.id, 'email': user.email}}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    user = user_service.get_user_by_email(email)
    if user and check_password_hash(user.password_hash, password):
        # Fetch all roles for the user
        user_org_roles = UserOrganizationRoleRepository().model.query.filter_by(user_id=user.id).all()
        roles = [Role.query.get(uor.role_id).name for uor in user_org_roles]
        access_token = create_access_token(identity=str(user.id), additional_claims={"roles": roles})
        return jsonify({
            'message': 'Login successful',
            'access_token': access_token,
            'user': {'id': user.id, 'email': user.email, 'roles': roles}
        })
    return jsonify({'error': 'Invalid credentials'}), 401
