#!/usr/bin/python3
"""
This module defines the `BaseModel` class, serving as the foundation for all
data models in the application, providing unique IDs and timestamps.
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    A base class for all models, providing initialization, serialization,
    and representation methods.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of BaseModel, setting ID and timestamps.
        Optionally, accepts keyword arguments to set attributes dynamically.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ("created_at", "updated_at"):
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)

        models.storage.new(self)

    def save(self):
        """Updates `updated_at` timestamp and calls storage save method."""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance,
        including the class name and formatted datetime objects.
        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()

        return inst_dict

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance,
        including the class name, ID, and dictionary of attributes.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print("JSON of my_model:")
    for key in my_model_json:
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))
    print("--")
    print(my_model is my_new_model)
