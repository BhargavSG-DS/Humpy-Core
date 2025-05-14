from app.core.database import database
from app.core.security import get_password_hash
from app.schemas.user import UserCreate

async def create_user(user: UserCreate) -> dict:
    """Create a new user with hashed password.

    Args:
        user (UserCreate): User data including email and password.

    Returns:
        dict: Created user data (id and email).
    """
    hashed_password = get_password_hash(user.password)
    query = """
        INSERT INTO users (email, hashed_password)
        VALUES (:email, :hashed_password)
        RETURNING id, email
    """
    values = {"email": user.email, "hashed_password": hashed_password}
    result = await database.fetch_one(query=query, values=values)
    return dict(result)

async def get_user(user_id: int) -> dict:
    """Retrieve a user by ID.

    Args:
        user_id (int): ID of the user to retrieve.

    Returns:
        dict: User data or None if not found.
    """
    query = "SELECT id, email FROM users WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": user_id})