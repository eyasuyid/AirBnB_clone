#!/usr/bin/python3
"""BaseModel module"""
import uuid
import datetime
import models


class BaseModel:
    """class BaseModel"""

    def __init__(self, *args, **kwargs):
        """__init__ method for BaseModel class
        Args:
            args (tuple): arguments
            kwargs (dict): key word arguments
        """
        if kwargs:
            for name, value in kwargs.items():
                if name != '__class__':
                    if name == 'created_at' or name == 'updated_at':
                        value = datetime.datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, name, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """string representation of BaseModel"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """save method of BaseModel updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """to_dict method of BaseModel creates dict with all keys/values of
        __dict__ of the instance
        Returns:
            dictionary of instance key-value pairs
        """
        base_dict = dict(self.__dict__)
        base_dict['__class__'] = type(self).__name__
        base_dict['created_at'] = base_dict['created_at'].isoformat()
        base_dict['updated_at'] = base_dict['updated_at'].isoformat()
        return base_dict
