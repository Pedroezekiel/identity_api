from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.user_org_role_service import UserOrgRoleService
from app.repositories.user_org_role_repository import UserOrganizationRoleRepository

user_org_role_bp = Blueprint('user_org_role', __name__, url_prefix='/api/user-org-roles')
user_org_role_service = UserOrgRoleService(UserOrganizationRoleRepository())

@user_org_role_bp.route('/', methods=['POST'])
@jwt_required()
def assign_role():
    data = request.get_json()
    user_id = data.get('user_id')
    org_id = data.get('org_id')
    role_id = data.get('role_id')
    if not user_id or not org_id or not role_id:
        return jsonify({'error': 'user_id, org_id, and role_id are required'}), 400
    user_org_role = user_org_role_service.assign_role(user_id, org_id, role_id)
    return jsonify({'id': user_org_role.id, 'user_id': user_org_role.user_id, 'org_id': user_org_role.org_id, 'role_id': user_org_role.role_id}), 201

@user_org_role_bp.route('/<int:user_org_role_id>', methods=['GET'])
@jwt_required()
def get_user_org_role(user_org_role_id):
    user_org_role = user_org_role_service.user_org_role_repository.get_by_id(user_org_role_id)
    if not user_org_role:
        return jsonify({'error': 'UserOrgRole not found'}), 404
    return jsonify({'id': user_org_role.id, 'user_id': user_org_role.user_id, 'org_id': user_org_role.org_id, 'role_id': user_org_role.role_id})

@user_org_role_bp.route('/', methods=['GET'])
@jwt_required()
def get_user_org_roles():
    user_org_roles = user_org_role_service.user_org_role_repository.get_all()
    return jsonify([
        {'id': uor.id, 'user_id': uor.user_id, 'org_id': uor.org_id, 'role_id': uor.role_id}
        for uor in user_org_roles
    ])

@user_org_role_bp.route('/<int:user_org_role_id>', methods=['PUT'])
@jwt_required()
def update_user_org_role(user_org_role_id):
    data = request.get_json()
    role_id = data.get('role_id')
    user_org_role = user_org_role_service.update_user_role(user_org_role_id, role_id)
    if not user_org_role:
        return jsonify({'error': 'UserOrgRole not found'}), 404
    return jsonify({'id': user_org_role.id, 'user_id': user_org_role.user_id, 'org_id': user_org_role.org_id, 'role_id': user_org_role.role_id})

@user_org_role_bp.route('/<int:user_org_role_id>', methods=['DELETE'])
@jwt_required()
def delete_user_org_role(user_org_role_id):
    result = user_org_role_service.delete_user_role(user_org_role_id)
    if not result:
        return jsonify({'error': 'UserOrgRole not found'}), 404
    return jsonify({'message': 'UserOrgRole deleted'})

