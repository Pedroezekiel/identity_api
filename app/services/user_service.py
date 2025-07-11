from werkzeug.security import generate_password_hash

from app.models import User


class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def register_user(self, email, password):
        if self.user_repository.get_by_email(email):
            raise ValueError("User already exists")

        hashed_password = self.hash_password(password)
        return self.user_repository.create(email=email, password_hash=hashed_password)

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password, method='pbkdf2:sha256')

    def get_user_by_email(self, email):
        return self.user_repository.get_by_email(email)
