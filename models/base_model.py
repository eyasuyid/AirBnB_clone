#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """ User class"""

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        else:
            self.id = kwargs['id']
            self.created_at = datetime.strptime(
                kwargs
                ['created_at'], "%Y-%m-%dT%H:%M:%S.%f"
            )
            self.updated_at = datetime.strptime(
                kwargs
                ['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"
            )

    def __str__(self):
        """ return the tring represantaion of an instance """
        return "[{}] ({}) {}".format(
            __class__.__name__,
            self.id, self.__dict__
        )

    def save(self):
        """ update the update time with the current time"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """ Return a  dectionary containing all keys"""

        created_at = self.created_at.isoformat()
        updated_at = self.updated_at.isoformat()

        dic = self.__dict__
        dic['__class__'] = __class__.__name__
        dic['created_at'] = created_at
        dic['updated_at'] = updated_at
        return dic
