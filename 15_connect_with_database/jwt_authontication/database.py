from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL  = os.getenv("DATABASE_URL")
engine = create_engine(SQLALCHEMY_DATABASE_URL)

sessionlocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)


Base = declarative_base()


def get_db():
    db = sessionlocal()
    
    try:
        yield db
        
    finally:
        db.close()