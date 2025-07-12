# Identity Management API

A full-featured identity management system built with Flask, supporting user authentication, organization management, role-based access control, invitations, and user-role assignments.

## Features

- **User Authentication**: Register and login with JWT-based authentication.
- **Organization Management**: Create, read, update, and delete organizations.
- **Role Management**: Define roles and assign them to users within organizations.
- **User-Organization-Role Assignment**: Assign roles to users in specific organizations.
- **Invitation Flow**: Invite users to organizations with specific roles and allow them to accept invitations.
- **Predefined Roles**: The system uses predefined roles (e.g., `ADMIN`, `MEMBER`, etc.) managed as an enum for consistency and security. These roles are seeded into the database and referenced throughout the application for access control and assignment.

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

- `/api/auth/register` - Register a new user
- `/api/auth/login` - Login and receive JWT token
- `/api/organizations/` - CRUD for organizations
- `/api/roles/` - CRUD for roles
- `/api/user-org-roles/` - Assign and manage user roles in organizations
- `/api/invitations/` - Send, accept, and manage invitations

All endpoints (except registration/login) require JWT authentication.

## Roles

- Predefined roles are available (e.g., `ADMIN`, `MEMBER`, etc.) and managed as an enum in the codebase.
- Roles are assigned to users within organizations and included in JWT tokens for authorization.
- You can extend or customize roles as needed in the enum and seed logic.

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
