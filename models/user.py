#!/usr/bin/python3
"""
This module defines the User class which inherits from BaseModel and Base (SQLAlchemy)
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class User(BaseModel, Base):
    """ User class that inherits from BaseModel and Base (from SQLAlchemy) """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    # Additional methods and attributes can be added below if needed
