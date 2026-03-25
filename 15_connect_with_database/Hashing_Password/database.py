from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")


# create_engine() is used to connect Python to the database.
# 🔌 Engine = Bridge between your Python app and your Database
engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush = False,
    bind=engine
)


# declarative_base() is used to create a base class for our models (tables).
Base = declarative_base()




def get_db():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()