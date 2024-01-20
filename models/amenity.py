#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.place import place_amenity
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity Class
       - Inherits from SQLAlchemy Base
       - links to MYSQL table amenities
    Attributes:
        __tablename__(str): name of MYSQL table to store Amenities
        name: represents amenity name
        place_amenities: relationship between Place and Amenity
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity,
                                   viewonly=False)
