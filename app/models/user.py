from sqlalchemy import Column, Integer, String
from app.core.database import metadata

class User:
    """SQLAlchemy model for users table."""
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}  # For Alembic compatibility

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)