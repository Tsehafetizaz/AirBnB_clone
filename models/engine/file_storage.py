#!/usr/bin/python3
"""Simple definition of the FileStorage class."""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Handles storage of HBnB models in JSON format."""

    __file_path = "file.json"  # Path to the JSON file
    __objects = {}  # Dictionary to store objects

    def all(self):
        """Returns the dictionary of stored objects."""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes stored objects to the JSON file."""
        with open(self.__file_path, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects, if file exists."""
        try:
            with open(self.__file_path) as f:
                for obj in json.load(f).values():
                    cls = eval(obj["__class__"])
                    del obj["__class__"]
                    self.new(cls(**obj))
        except FileNotFoundError:
            pass
