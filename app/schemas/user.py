from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    """Base schema for user data."""
    email: EmailStr

class UserCreate(UserBase):
    """Schema for creating a new user."""
    password: str

class User(UserBase):
    """Schema for user response."""
    id: int

    class Config:
        orm_mode = True  # Enables compatibility with SQLAlchemy models