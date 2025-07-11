from app.db import db

class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    # Relationships
    user_org_roles = db.relationship("UserOrganizationRole", back_populates="role")
