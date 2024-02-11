#!/usr/bin/python3
"""
This module defines the FileStorage class for serializing instances
to a JSON file and deserializing JSON file to instances.
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class FileStorage:
    """
    Handles long-term storage of all class instances via serialization
    to JSON and deserialization from JSON.
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.

        Args:
            obj: The object to add, which must have an 'id' attribute.
        """
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def all(self):
        """
        Returns a dictionary of all stored objects.

        Returns:
            A dictionary copy of __objects.
        """
        return self.__objects

    def save(self):
        """
        Serializes __objects to the JSON file (__file_path).
        """
        obj_dict = {
            obj: self.__objects[obj].to_dict()
            for obj in self.__objects
        }
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects, if __file_path exists.
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                try:
                    obj_dict = json.load(f)
                    for key, value in obj_dict.items():
                        cls_name = value['__class__']
                        cls = eval(cls_name)
                        self.__objects[key] = cls(**value)
                except Exception:
                    pass
