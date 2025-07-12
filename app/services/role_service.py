from app.repositories.role_repository import RoleRepository

class RoleService:
    def __init__(self, role_repository: RoleRepository):
        self.role_repository = role_repository

    def create_role(self, name):
        # Allow both predefined and custom roles
        return self.role_repository.create(name=name)

    def get_role(self, role_id):
        return self.role_repository.get_by_id(role_id)

    def get_all_roles(self):
        return self.role_repository.get_all()

    def update_role(self, role_id, name):
        role = self.role_repository.get_by_id(role_id)
        if not role:
            return None
        return self.role_repository.update(role, name=name)

    def delete_role(self, role_id):
        return self.role_repository.delete(role_id)

    def seed_predefined_roles(self):
        from app.models.role_enum import RoleEnum
        for role in RoleEnum:
            if not self.role_repository.get_by_name(role.value):
                self.role_repository.create(name=role.value)
