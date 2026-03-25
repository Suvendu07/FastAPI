"""This file contains the database connection details and session configuration, which tells the application where and how to connect to the database."""


"""
create_engine is used to create a connection bridge between your Python app and the database.

What it does

Knows which database to connect to (PostgreSQL, MySQL, etc.)

Knows where the database is (host, port, db name)

Sends SQL queries to the database"""



"""create_engine connects database with SQLAlchemy (ORM) code written in Python, declarative_base tells SQLAlchemy which Python classes represent database tables, and sessionmaker manages database sessions to execute queries and handle opening and closing connections."""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os



"""It is a database connection URL that tells SQLAlchemy:

which database type (PostgreSQL)

username & password

host

database name"""
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")


# The engine creates a connection interface between SQLAlchemy (ORM/Core code) and the database.
engine = create_engine(SQLALCHEMY_DATABASE_URL)



# SessionLocal is a factory that creates database sessions used to run queries and manage transactions.
SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
        
    finally:
        db.close()