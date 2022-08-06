#!/usr/bin/python3
""" FileStorage module """


import json


class FileStorage:
    """ FileStorage class """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            Function that returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
            Function that sets in __objects the obj with key
            <obj class name>.id
        """
        FileStorage.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """
            Function that serializes __objects to the JSON file
            (path: __file_path)
        """
        dict = {}
        for key, value in FileStorage.__objects.items():
            dict[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(dict, file)

    def reload(self):
        """
            deserializes the JSON file to __objects (only if the JSON file
            (__file_path) exists ; otherwise, do nothing. If the file doesn’t
            exist, no exception should be raised)
        """
        try:
            from models.base_model import BaseModel
            from models.user import User
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.place import Place
            from models.review import Review
            with open(FileStorage.__file_path, 'r') as file:
                for key, value in json.load(file).items():
                    className = value['__class__']
                    FileStorage.__objects[key] = eval(className)(**value)
        except Exception:
            pass
