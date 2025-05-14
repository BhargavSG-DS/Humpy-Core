from fastapi import APIRouter, HTTPException
from app.schemas.user import User, UserCreate
from app.services.user_service import create_user, get_user

router = APIRouter()

@router.post("/", response_model=User, status_code=201)
async def create_user_endpoint(user: UserCreate):
    """Create a new user.

    Args:
        user (UserCreate): User data to create.

    Returns:
        User: Created user data.

    Raises:
        HTTPException: If email already exists (duplicate key error).
    """
    try:
        return await create_user(user)
    except Exception:  # Simplified error handling for brevity
        raise HTTPException(status_code=400, detail="Email already registered")

@router.get("/{user_id}", response_model=User)
async def get_user_endpoint(user_id: int):
    """Retrieve a user by ID.

    Args:
        user_id (int): ID of the user to retrieve.

    Returns:
        User: User data.

    Raises:
        HTTPException: If user not found.
    """
    user = await get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user