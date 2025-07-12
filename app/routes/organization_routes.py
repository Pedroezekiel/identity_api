from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.organization_service import OrganizationService
from app.repositories.organization_repository import OrganizationRepository
from app.services.user_org_role_service import UserOrgRoleService
from app.repositories.user_org_role_repository import UserOrganizationRoleRepository
from app.models.role import Role
from app import db

organization_bp = Blueprint('organization', __name__, url_prefix='/api/organizations')
organization_service = OrganizationService(OrganizationRepository())
user_org_role_service = UserOrgRoleService(UserOrganizationRoleRepository())

@organization_bp.route('/', methods=['POST'])
@jwt_required()
def create_organization():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    if not name:
        return jsonify({'error': 'Name is required'}), 400
    try:
        # Assign OWNER role to the creator
        user_id = int(get_jwt_identity())
        org = organization_service.create_organization(name=name, description=description, user_id=user_id)
        owner_role = Role.query.filter_by(name="OWNER").first()
        if owner_role:
            user_org_role_service.assign_role(user_id, org.id, owner_role.id)
        return jsonify({'id': org.id, 'name': org.name, 'description': org.description}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@organization_bp.route('/<int:org_id>', methods=['GET'])
@jwt_required()
def get_organization(org_id):
    org = organization_service.get_organization(org_id)
    if not org:
        return jsonify({'error': 'Organization not found'}), 404
    return jsonify({'id': org.id, 'name': org.name, 'description': org.description})

@organization_bp.route('/', methods=['GET'])
@jwt_required()
def get_organizations():
    orgs = organization_service.get_all_organizations()
    return jsonify([{'id': org.id, 'name': org.name, 'description': org.description} for org in orgs])

@organization_bp.route('/<int:org_id>', methods=['PUT'])
@jwt_required()
def update_organization(org_id):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    org = organization_service.update_organization(org_id, name, description)
    if not org:
        return jsonify({'error': 'Organization not found'}), 404
    return jsonify({'id': org.id, 'name': org.name, 'description': org.description})

@organization_bp.route('/<int:org_id>', methods=['DELETE'])
@jwt_required()
def delete_organization(org_id):
    org = organization_service.delete_organization(org_id)
    if not org:
        return jsonify({'error': 'Organization not found'}), 404
    return jsonify({'message': 'Organization deleted', 'id': org.id})
