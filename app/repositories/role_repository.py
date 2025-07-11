from app.repositories.base_repository import BaseRepository
from app.models.role import Role

class RoleRepository(BaseRepository):
    def __init__(self):
        super().__init__(Role)

    @staticmethod
    def get_by_name(name):
        return Role.query.filter_by(name=name).first()
