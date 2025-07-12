from app.repositories.user_org_role_repository import UserOrganizationRoleRepository

class UserOrgRoleService:
    def __init__(self, user_org_role_repository: UserOrganizationRoleRepository):
        self.user_org_role_repository = user_org_role_repository

    def assign_role(self, user_id, organization_id, role_id):
        return self.user_org_role_repository.create(user_id=user_id, organization_id=organization_id, role_id=role_id)

    def get_user_roles(self, user_id, org_id=None):
        return self.user_org_role_repository.find_by_user_and_org(user_id, org_id)

    def update_user_role(self, user_org_role_id, role_id):
        user_org_role = self.user_org_role_repository.get_by_id(user_org_role_id)
        if not user_org_role:
            return None
        return self.user_org_role_repository.update(user_org_role, role_id=role_id)

    def delete_user_role(self, user_org_role_id):
        user_org_role = self.user_org_role_repository.get_by_id(user_org_role_id)
        if not user_org_role:
            return None
        self.user_org_role_repository.delete(user_org_role)
        return True
