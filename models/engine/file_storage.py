#!/usr/bin/python3
"""Defines the FileStorage class."""
import json


class FileStorage:
    """Serializes instances to JSON file deserializes JSON file instances"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {
            obj: FileStorage.__objects[obj].to_dict()
            for obj in FileStorage.__objects.keys()
        }
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objs = json.load(f)
            for obj in objs.values():
                class_name = obj['__class__']
                del obj['__class__']
                self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            pass
