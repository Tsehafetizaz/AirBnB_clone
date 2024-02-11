#!/usr/bin/python3
"""BaseModel for HBnB project."""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Defines the base model for all HBnB objects."""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance.

        Args:
            *args: Unused.
            **kwargs: Key-value pairs for initializing attributes.
        """
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def save(self):
        """Updates `updated_at` with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Converts instance to a dictionary format, including class name."""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return obj_dict

    def __str__(self):
        """String representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
