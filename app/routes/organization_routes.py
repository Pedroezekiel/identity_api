from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.organization_service import OrganizationService
from app.repositories.organization_repository import OrganizationRepository
from app import db

organization_bp = Blueprint('organization', __name__, url_prefix='/api/organizations')
organization_service = OrganizationService(OrganizationRepository())

@organization_bp.route('/', methods=['POST'])
@jwt_required()
def create_organization():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({'error': 'Name is required'}), 400
    try:
        org = organization_service.create_organization(name)
        return jsonify({'id': org.id, 'name': org.name}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@organization_bp.route('/<int:org_id>', methods=['GET'])
@jwt_required()
def get_organization(org_id):
    org = organization_service.get_organization(org_id)
    if not org:
        return jsonify({'error': 'Organization not found'}), 404
    return jsonify({'id': org.id, 'name': org.name})

@organization_bp.route('/', methods=['GET'])
@jwt_required()
def get_organizations():
    orgs = organization_service.get_all_organizations()
    return jsonify([{'id': org.id, 'name': org.name} for org in orgs])

@organization_bp.route('/<int:org_id>', methods=['PUT'])
@jwt_required()
def update_organization(org_id):
    data = request.get_json()
    name = data.get('name')
    org = organization_service.update_organization(org_id, name)
    if not org:
        return jsonify({'error': 'Organization not found'}), 404
    return jsonify({'id': org.id, 'name': org.name})

@organization_bp.route('/<int:org_id>', methods=['DELETE'])
@jwt_required()
def delete_organization(org_id):
    org = organization_service.delete_organization(org_id)
    if not org:
        return jsonify({'error': 'Organization not found'}), 404
    return jsonify({'message': 'Organization deleted', 'id': org.id})
