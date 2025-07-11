
from app.db import db

class UserOrganizationRole(db.Model):
    __tablename__ = "user_organization_roles"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    organization_id = db.Column(db.Integer, db.ForeignKey("organizations.id"), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)

    # Relationships
    user = db.relationship("User", back_populates="user_org_roles")
    organization = db.relationship("Organization", back_populates="user_org_roles")
    role = db.relationship("Role", back_populates="user_org_roles")
