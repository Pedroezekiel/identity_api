from app import create_app
from app.db import db
from app.models import User
from app.repositories.user_repository import UserRepository

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "User": User,
        "user_repo": UserRepository()
    }

if __name__ == "__main__":
    app.run(debug=True)
