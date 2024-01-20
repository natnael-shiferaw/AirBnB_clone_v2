#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from models.place import Place
from models.review import Review
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """User class
       - Inherits from SQLAlchemy Base
       - links to MYSQL table user
    Attributes:
        __tablename__(str): name of MYSQL table to store users 
        email: user's email address
        password: user's password for you login
        first_name: user's first name
        last_name: user's last name
        places : relationship between User and Place
        reviews: relationship between User and Review
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="user")
