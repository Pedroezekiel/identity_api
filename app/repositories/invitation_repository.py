from app.repositories.base_repository import BaseRepository
from app.models.invitation import Invitation

class InvitationRepository(BaseRepository):
    def __init__(self):
        super().__init__(Invitation)

    @staticmethod
    def get_by_token(token):
        return Invitation.query.filter_by(token=token).first()
