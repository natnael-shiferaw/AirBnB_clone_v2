#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Review(BaseModel, Base):
    """Review Class
       - Inherits from SQLAlchemy Base
       - links to MYSQL table review
    Attributes:
        __tablename__(str): name of MYSQL table to store Reviews
        place_id: review's place id
        user_id: review's user id
        text: represents review description
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
