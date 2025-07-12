from app.repositories.invitation_repository import InvitationRepository

class InvitationService:
    def __init__(self, invitation_repository: InvitationRepository):
        self.invitation_repository = invitation_repository

    def send_invitation(self, email, org_id, role_id, inviter_id):
        return self.invitation_repository.create(email=email, org_id=org_id, role_id=role_id, inviter_id=inviter_id)

    def get_invitation(self, invitation_id):
        return self.invitation_repository.get_by_id(invitation_id)

    def get_all_invitations(self):
        return self.invitation_repository.get_all()

    def accept_invitation(self, invitation_id, user_id):
        invitation = self.invitation_repository.get_by_id(invitation_id)
        if not invitation:
            return None
        # Mark invitation as accepted and assign role
        self.invitation_repository.update(invitation, accepted=True, accepted_by=user_id)
        return invitation

    def delete_invitation(self, invitation_id):
        invitation = self.invitation_repository.get_by_id(invitation_id)
        if not invitation:
            return None
        self.invitation_repository.delete(invitation)
        return True

