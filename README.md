# Identity Management API

A robust identity management system built with Flask, supporting user authentication, organization management, role-based access control, invitations, and user-role assignments.

## Features

- **User Authentication**: Register and login with JWT-based authentication.
- **Organization Management**: Create, read, update, and delete organizations. Each user can only create one organization. Organization names must be unique. Organizations support an optional description field.
- **Role Management**: Predefined roles (e.g., `ADMIN`, `MEMBER`, `OWNER`) managed as an enum, plus support for custom roles. Roles are seeded on startup and can be assigned to users within organizations.
- **User-Organization-Role Assignment**: Assign roles to users in specific organizations. The creator of an organization is automatically assigned the `OWNER` role.
- **Invitation Flow**: Invite users to organizations with specific roles and custom metadata. Invitations can be accepted and include flexible fields.

## Project Structure

```
app/
  __init__.py            # App factory, blueprint registration
  db.py                  # Database setup
  models/                # SQLAlchemy models (User, Role, Organization, Invitation, UserOrgRole)
  repositories/          # CRUD logic for each model
  services/              # Business logic for each entity
  routes/                # API endpoints for each entity
config/
  config.py              # App configuration
run.py                   # App entry point
```

## API Endpoints

### Auth
- `POST /api/auth/register` — Register a new user
- `POST /api/auth/login` — Login and receive JWT token

### Organization
- `POST /api/organizations/` — Create an organization (with optional description, assigns OWNER role)
- `GET /api/organizations/` — List all organizations
- `GET /api/organizations/<org_id>` — Get details of a specific organization
- `PUT /api/organizations/<org_id>` — Update an organization (name, description)
- `DELETE /api/organizations/<org_id>` — Delete an organization

### Role
- `POST /api/roles/` — Create a role (predefined or custom)
- `GET /api/roles/` — List all roles
- `GET /api/roles/<role_id>` — Get details of a specific role
- `PUT /api/roles/<role_id>` — Update a role
- `DELETE /api/roles/<role_id>` — Delete a role

### User-Organization-Role
- `POST /api/user-org-roles/` — Assign a role to a user in an organization
- `GET /api/user-org-roles/` — List all user-org-role assignments
- `GET /api/user-org-roles/<user_org_role_id>` — Get details of a specific assignment
- `PUT /api/user-org-roles/<user_org_role_id>` — Update a user-org-role assignment
- `DELETE /api/user-org-roles/<user_org_role_id>` — Delete a user-org-role assignment

### Invitation
- `POST /api/invitations/` — Send an invitation (supports custom fields)
- `GET /api/invitations/` — List all invitations
- `GET /api/invitations/<invitation_id>` — Get details of a specific invitation
- `POST /api/invitations/<invitation_id>/accept` — Accept an invitation
- `DELETE /api/invitations/<invitation_id>` — Delete an invitation

All endpoints (except registration/login) require JWT authentication.

## Roles

- Predefined roles are available (e.g., `ADMIN`, `MEMBER`, `OWNER`) and managed as an enum in the codebase.
- Roles are assigned to users within organizations and included in JWT tokens for authorization.
- You can extend or customize roles as needed in the enum and seed logic.

## Organization Rules

- Each user can create only one organization.
- Organization names must be unique.
- The creator is automatically assigned the `OWNER` role.
- Organizations support an optional description field.

## Getting Started

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
2. **Configure environment**
   - Copy `.env.example` to `.env` and set your environment variables.
3. **Run the app**
   ```bash
   python run.py
   ```

## Usage

- Use Postman or similar tools to interact with the API.
- Register/login to obtain a JWT token.
- Use the token as a Bearer token for authenticated requests.

## Extending

- Add permissions, audit logs, or custom business logic as needed.
- Integrate with external identity providers if required.

## License

MIT
