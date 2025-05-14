from databases import Database
from sqlalchemy import create_engine, MetaData
from app.core.config import settings

# Database connection for async queries
database = Database(settings.DATABASE_URL)

# SQLAlchemy engine for model definitions and migrations
engine = create_engine(settings.DATABASE_URL)
metadata = MetaData()

async def connect():
    """Establish database connection."""
    await database.connect()

async def disconnect():
    """Close database connection."""
    await database.disconnect()