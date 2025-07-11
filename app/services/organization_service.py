from app.repositories.organization_repository import OrganizationRepository
from app.models.organization import Organization

class OrganizationService:
    def __init__(self, organization_repository=None):
        self.organization_repository = organization_repository or OrganizationRepository()

    def create_organization(self, name):
        if self.organization_repository.model.query.filter_by(name=name).first():
            raise ValueError("Organization already exists")
        return self.organization_repository.create(name=name)

    def get_organization(self, org_id):
        return self.organization_repository.get_by_id(org_id)

    def get_all_organizations(self):
        return self.organization_repository.model.query.all()

    def update_organization(self, org_id, name):
        org = self.organization_repository.get_by_id(org_id)
        if not org:
            return None
        org.name = name
        self.organization_repository.save(org)
        return org

    def delete_organization(self, org_id):
        org = self.organization_repository.get_by_id(org_id)
        if not org:
            return None
        self.organization_repository.delete(org)
        return org

