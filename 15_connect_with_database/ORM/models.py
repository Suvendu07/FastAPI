"""We usually avoid direct SQL queries because they are more error-prone, vulnerable to SQL injection, harder to maintain, and tightly coupled to a specific database. ORMs provide safer, cleaner, and more maintainable database interaction."""


"""This file defines the structure of the tables(col, types, constraints) that will be created inside the database."""



from .database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.sql import func



class Post(Base):
    __tablename__ = 'suvendu'
    
    id = Column(Integer, primary_key=True, nullable = False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable=False, server_default='True')
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    