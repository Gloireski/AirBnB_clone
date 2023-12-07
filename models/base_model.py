#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self):
        """Initialize a new BaseModel."""
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__

    def __str__(self):
        """Return the print/str representation of the BaseModel instance"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
=======
""" a class BaseModel that defines all
attributes and methodes for other classes """

from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """the desined BaseModel class """
    def __init__(self, *args, **kwargs):
        ''' Inintializing BaseModel istance'''
        if kwargs:
            for key, value in kwargs.items():
                if key =='created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        ''' returns a string representation of BaseModel instance'''
        return  "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        ''' apdates the public instance attribute withe the current datetime'''
        self.updated_at = datetime.now()
    def to_dict(self):
        ''' returns a dictionary containing all keys/values of __dict__ of the instance'''
        dict_format = self.__dict__.copy()
        dict_format['created_at'] = self.created_at.isoformat()
        dict_format['uppdated_at'] = self.uppdated_at.isoformat()
        dict_format['__class__'] = self.__class__.__name__
        return dict_format
        
>>>>>>> fd2b74ba8e2a33b91d3c205ebf53c6b26426069f
