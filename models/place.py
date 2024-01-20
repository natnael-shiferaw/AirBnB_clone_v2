#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.amenity import Amenity
from models.review import Review


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """Place Class
       - Inherits from SQLAlchemy Base
       - links to MYSQL table places
    Attributes:
        __tablename__(str): name of MYSQL table to store places
        city_id: place's city id
        user_id: place's user id
        name: represents the name
        description: represents the description
        number_rooms: represents the number of rooms
        number_bathrooms: represents the number of bathrooms
        max_guest: represents maximum number of guests
        price_by_night: represents the price by the night
        latitude: place's latitude
        longitude: place's longitude
        amenity_ids: represents the list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")
    amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """ Returns list of related Reviews """
            list_of_reviews = []
            reviews = list(models.storage.all(Review).values())
            for review in reviews:
                if review.place_id == self.id:
                    list_of_reviews.append(review)
            return list_of_reviews

        @property
        def amenities(self):
            """ Returns list of related amenities"""
            list_of_amenities = []
            amenities = list(models.storage.all(Amenity).values())
            for amenity in amenities:
                if amenity.id in self.amenity_ids:
                    list_of_amenities.append(amenity)
            return list_of_amenities

        @amenities.setter
        def amenities(self, obj=None):
            """ Appends amenity ids to the attribute """
            if type(obj) == Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
