from app.repositories.base_repository import BaseRepository
from app.models.organization import Organization

class OrganizationRepository(BaseRepository):
    def __init__(self):
        super().__init__(Organization)
