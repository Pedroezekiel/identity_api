from app.repositories.base_repository import BaseRepository
from app.models.user import User

class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()
