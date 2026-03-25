from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from .config import settings

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{settings.DB_USER}:"
    f"{settings.DB_PASSWORD}@"
    f"{settings.DB_HOST}:"
    f"{settings.DB_PORT}/"
    f"{settings.DB_NAME}"
)



engine = create_engine(SQLALCHEMY_DATABASE_URL)

sessionlocal = sessionmaker(autoflush=False, autocommit = False, bind=engine)

Base = declarative_base()


def get_db():
    db = sessionlocal()
    
    try:
        yield db
    
    finally:
        db.close()