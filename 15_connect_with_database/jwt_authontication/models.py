from sqlalchemy import Column, String, Integer
from .database import Base, engine


class suvendu(Base):
    
    __tablename__ = "babul"
    
    id = Column(Integer, nullable=False, primary_key=True, unique=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable= False)
    password = Column(String, nullable=False, unique=True)
