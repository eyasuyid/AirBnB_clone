#!/usr/bin/python3
"""FileStorage module"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """class FileStorage

    Attributes:
        __filepath (str): file path to JSON file
        __objects (dict): dictionary of objects
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """all method returns dictionary of objects
        Returns:
            __objects - dictionary of objects
        """
        return self.__objects

    def new(self, obj):
        """new method which adds object to __objects dict
        Args:
            obj (object): object to add to dictionary
        """
        if obj:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """save method serializes __objects to JSON file at __filepath"""
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()

        json_str = json.dumps(obj_dict)

        with open(self.__file_path, 'w', encoding='utf-8') as f:
            f.write(json_str)

    def reload(self):
        """reload method deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                json_dict = json.load(f)
                for obj_dict in json_dict.values():
                    cls = obj_dict['__class__']
                    self.new(eval('{}({})'.format(cls, '**obj_dict')))
        except FileNotFoundError:
            pass
