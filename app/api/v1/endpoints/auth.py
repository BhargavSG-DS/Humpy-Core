from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import verify_password, create_access_token
from app.services.user_service import get_user_by_email  # Assume this exists
from datetime import timedelta

router = APIRouter()

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """Authenticate user and return JWT token.

    Args:
        form_data (OAuth2PasswordRequestForm): Username (email) and password.

    Returns:
        dict: Access token and token type.

    Raises:
        HTTPException: If credentials are invalid.
    """
    user = await get_user_by_email(form_data.username)  # Simplified; implement this
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": str(user["id"])}, expires_delta=timedelta(minutes=30))
    return {"access_token": access_token, "token_type": "bearer"}