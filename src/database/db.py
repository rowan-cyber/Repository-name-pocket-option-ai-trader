"""
Database initialization
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config.settings import settings
from src.database.models import Base

# Create engine
engine = create_engine(settings.database_url, echo=False)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """
    Initialize database
    """
    Base.metadata.create_all(bind=engine)

def get_db():
    """
    Get database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
