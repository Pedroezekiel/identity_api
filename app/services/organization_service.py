from app.repositories.organization_repository import OrganizationRepository
from app.models.organization import Organization
from app.models.user_org_role import UserOrganizationRole
from app.db import db

class OrganizationService:
    def __init__(self, organization_repository=None):
        self.organization_repository = organization_repository or OrganizationRepository()

    def create_organization(self, name, description=None, user_id=None):
        # Prevent user from creating more than one organization
        user_orgs = UserOrganizationRole.query.filter_by(user_id=user_id).all()
        if user_orgs:
            raise ValueError("User cannot create more than one organization.")
        # Prevent duplicate organization name
        existing_org = Organization.query.filter_by(name=name).first()
        if existing_org:
            raise ValueError("An organization with this name already exists.")
        org = self.organization_repository.create(name=name, description=description, created_by=user_id)
        return org

    def get_organization(self, org_id):
        return self.organization_repository.get_by_id(org_id)

    def get_all_organizations(self):
        return self.organization_repository.model.query.all()

    def update_organization(self, org_id, name=None, description=None):
        org = self.organization_repository.get_by_id(org_id)
        if not org:
            return None
        if name:
            org.name = name
        if description is not None:
            org.description = description
        db.session.commit()
        return org

    def delete_organization(self, org_id):
        org = self.organization_repository.get_by_id(org_id)
        if not org:
            return None
        self.organization_repository.delete(org)
        return org
