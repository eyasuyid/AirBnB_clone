#!/usr/bin/python3
"""Module for FileStorage class."""

import json
import os


class FileStorage:
    """ file storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return the dictionary _object"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        dkey = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[dkey] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file (path: __file_path) """
        if len(FileStorage.__objects) != 0:
            serial_objs = json.dumps(FileStorage.__objects)

            with open(FileStorage.__file_path, 'w') as f:
                f.write(serial_objs)

    def reload(self):
        """ deserializes the JSON file to __objects """
        FileStorage.__objects.clear()

        if not os.path.isfile(FileStorage.__file_path):
            return

        if os.path.getsize(FileStorage.__file_path) == 0:
            return

        with open(FileStorage.__file_path, "r") as f:
            FileStorage.__objects = json.loads(f.read())
