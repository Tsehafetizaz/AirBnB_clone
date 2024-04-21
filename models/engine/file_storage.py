#!/usr/bin/python3
"""
This module contains the FileStorage class for HBnB project.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """A class that serializes instances to a JSON file and deserializes JSON
    file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage.

        Args:
            cls: The class to filter objects by. If None, returns all objects.
        """
        if cls is None:
            return FileStorage.__objects
        else:
            filtered_objects = {}
            for key, value in FileStorage.__objects.items():
                if isinstance(value, cls):
                    filtered_objects[key] = value
            return filtered_objects

    def close(self):
        """Deserializes the JSON file to objects for reloading data."""
        self.__objects = self.reload()

    def new(self, obj):
        """Adds new object to storage dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (__file_path)."""
        obj_dict = {}
        for key in FileStorage.__objects:
            obj_dict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects, only if the JSON file
        (__file_path) exists."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objs = json.load(f)
            for obj in objs.values():
                cls_name = obj['__class__']
                del obj['__class__']
                self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects if it’s inside.

        Args:
            obj: The object to delete from storag, method does nothing.
        """
        if obj is not None:
            obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if obj_key in FileStorage.__objects:
                del FileStorage.__objects[obj_key]
