#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model.
        Args:
            args: it won't be used
            kwargs: key value pairs
        """
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for k,v in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, k, v)

    def __str__(self):
        """Returns a string representation of the instance"""
        my_dict = self.__dict__.copy()
        my_dict.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, my_dict)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format
        Return:
             returns a dictionary of all the key/values in __dict__
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = str(type(self).__name__)
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Delete current instance from the storage."""
        models.storage.delete(self)
