from pydantic import BaseSettings

class Settings(BaseSettings):
    """Application configuration settings loaded from environment variables."""
    DATABASE_URL: str  # e.g., postgresql://user:password@localhost:5432/dbname
    SECRET_KEY: str   # Secret key for JWT
    RAZORPAY_KEY_ID: str
    RAZORPAY_KEY_SECRET: str

    class Config:
        env_file = ".env"  # Load from .env file
        env_file_encoding = "utf-8"

# Singleton instance of settings
settings = Settings()