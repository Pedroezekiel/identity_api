# Identity Management API

A secure and modular Identity Management RESTful API built with Flask using Object-Oriented Programming (OOP) and layered architecture principles.

## 🚀 Features

- User, Role, and Organization management
- Invitation workflow to onboard users to organizations
- JWT-based authentication and authorization
- Role-based access control
- Layered architecture: Models, Repositories, Services, Controllers
- PostgreSQL as the database backend
- Postman for API testing

## 🧱 Tech Stack

- **Backend**: Python 3.11, Flask
- **Database**: PostgreSQL
- **Authentication**: JWT (Flask-JWT-Extended)
- **Testing**: Postman
- **Architecture**: OOP + Layered (MVC inspired)

## 🗂️ Project Structure

identity_api/
├── app/
│ ├── models/ # SQLAlchemy models (User, Role, Org, etc.)
│ ├── repositories/ # DB operations for each model
│ ├── services/ # Business logic
│ ├── controllers/ # Route definitions and handlers
│ ├── init.py # App factory
├── config/
│ └── config.py # Environment-based config
├── run.py # Entry point
├── requirements.txt # Dependencies

markdown
Copy code

## ✅ Planned Workflow

### 1. Project Setup
- Create virtual environment
- Install dependencies
- Setup base folder structure
- Create app factory (`create_app`)

### 2. Database Modeling
- User, Role, Organization, Invitation, UserOrgRole pivot model

### 3. Repository Layer
- CRUD operations encapsulated per entity

### 4. Service Layer
- Business logic:
  - Register/Login
  - Invite flow
  - Assign roles

### 5. Controller Layer
- Flask Blueprints:
  - `/auth` – Login, Register, Token refresh
  - `/org` – Create org, assign roles
  - `/invite` – Send and accept invitation

### 6. JWT Integration
- Protect endpoints
- Role-based access enforcement

### 7. Testing
- Postman collections
- Workflow testing (invite → join → assign)

## 📦 Installation

```bash
git clone https://github.com/your-username/identity-api.git
cd identity-api
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt