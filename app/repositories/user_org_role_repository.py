from app.repositories.base_repository import BaseRepository
from app.models.user_org_role import UserOrganizationRole

class UserOrganizationRoleRepository(BaseRepository):
    def __init__(self):
        super().__init__(UserOrganizationRole)

    @staticmethod
    def find_by_user_and_org(user_id, org_id):
        return UserOrganizationRole.query.filter_by(user_id=user_id, organization_id=org_id).first()
