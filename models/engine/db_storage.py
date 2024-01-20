#!/usr/bin/python3
"""This class manages storage of hbnb models in a database"""
from os import getenv
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session, relationship



class DBStorage:
    """ Represents database storage engine
    Attributes:
       __engine : SQLAlchemy engine
       __session : SQLAlchemy session
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initializes a new database storage instance"""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        env = getenv("HBNB_ENV")
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """If cls is None ,it queries all types of objects
        Return:
            returns a dictionary of queried classes
        """
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
                objs = self.__session.query(cls)
        else:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        return {f'{type(obj).__name__}.{obj.id}': obj for obj in objs}

    def new(self, obj):
        """add a new element in the table"""
        self.__session.add(obj)

    def save(self):
        """save changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete an element from the table"""
        if obj is not None:
            self.session.delete(obj)

    def reload(self):
        """Creates all the tables in the database,
        initializes a new session
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """ closes SQLAlchemy's working session
        """
        self.__session.close()
