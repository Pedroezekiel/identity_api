from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.invitation_service import InvitationService
from app.repositories.invitation_repository import InvitationRepository

invitation_bp = Blueprint('invitation', __name__, url_prefix='/api/invitations')
invitation_service = InvitationService(InvitationRepository())

@invitation_bp.route('/', methods=['POST'])
@jwt_required()
def send_invitation():
    data = request.get_json()
    email = data.get('email')
    org_id = data.get('org_id')
    role_id = data.get('role_id')
    inviter_id = data.get('inviter_id')
    if not email or not org_id or not role_id or not inviter_id:
        return jsonify({'error': 'email, org_id, role_id, and inviter_id are required'}), 400
    invitation = invitation_service.send_invitation(email, org_id, role_id, inviter_id)
    return jsonify({'id': invitation.id, 'email': invitation.email, 'org_id': invitation.org_id, 'role_id': invitation.role_id, 'inviter_id': invitation.inviter_id}), 201

@invitation_bp.route('/<int:invitation_id>', methods=['GET'])
@jwt_required()
def get_invitation(invitation_id):
    invitation = invitation_service.get_invitation(invitation_id)
    if not invitation:
        return jsonify({'error': 'Invitation not found'}), 404
    return jsonify({'id': invitation.id, 'email': invitation.email, 'org_id': invitation.org_id, 'role_id': invitation.role_id, 'inviter_id': invitation.inviter_id, 'accepted': getattr(invitation, 'accepted', False)})

@invitation_bp.route('/', methods=['GET'])
@jwt_required()
def get_invitations():
    invitations = invitation_service.get_all_invitations()
    return jsonify([
        {'id': inv.id, 'email': inv.email, 'org_id': inv.org_id, 'role_id': inv.role_id, 'inviter_id': inv.inviter_id, 'accepted': getattr(inv, 'accepted', False)}
        for inv in invitations
    ])

@invitation_bp.route('/<int:invitation_id>/accept', methods=['POST'])
@jwt_required()
def accept_invitation(invitation_id):
    data = request.get_json()
    user_id = data.get('user_id')
    invitation = invitation_service.accept_invitation(invitation_id, user_id)
    if not invitation:
        return jsonify({'error': 'Invitation not found'}), 404
    return jsonify({'message': 'Invitation accepted', 'id': invitation.id})

@invitation_bp.route('/<int:invitation_id>', methods=['DELETE'])
@jwt_required()
def delete_invitation(invitation_id):
    result = invitation_service.delete_invitation(invitation_id)
    if not result:
        return jsonify({'error': 'Invitation not found'}), 404
    return jsonify({'message': 'Invitation deleted'})

