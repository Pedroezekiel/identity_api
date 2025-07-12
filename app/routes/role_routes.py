from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.role_service import RoleService
from app.repositories.role_repository import RoleRepository

role_bp = Blueprint('role', __name__, url_prefix='/api/roles')
role_service = RoleService(RoleRepository())

@role_bp.route('/', methods=['POST'])
@jwt_required()
def create_role():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({'error': 'Name is required'}), 400
    role = role_service.create_role(name)
    return jsonify({'id': role.id, 'name': role.name}), 201

@role_bp.route('/<int:role_id>', methods=['GET'])
@jwt_required()
def get_role(role_id):
    role = role_service.get_role(role_id)
    if not role:
        return jsonify({'error': 'Role not found'}), 404
    return jsonify({'id': role.id, 'name': role.name})

@role_bp.route('/', methods=['GET'])
@jwt_required()
def get_roles():
    roles = role_service.get_all_roles()
    return jsonify([{'id': r.id, 'name': r.name} for r in roles])

@role_bp.route('/<int:role_id>', methods=['PUT'])
@jwt_required()
def update_role(role_id):
    data = request.get_json()
    name = data.get('name')
    role = role_service.update_role(role_id, name)
    if not role:
        return jsonify({'error': 'Role not found'}), 404
    return jsonify({'id': role.id, 'name': role.name})

@role_bp.route('/<int:role_id>', methods=['DELETE'])
@jwt_required()
def delete_role(role_id):
    result = role_service.delete_role(role_id)
    if not result:
        return jsonify({'error': 'Role not found'}), 404
    return jsonify({'message': 'Role deleted'})

