#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """Defines common attributes/methods for other classes."""

    def __init__(self):
        """Initializes a new instance of BaseModel."""
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string representation of the BaseModel instance."""
        return f"[{{self.__class__.__name__}}] ({self.id}) {{self.__dict__}}"

    def save(self):
        """Updates the instance's updated_at attribute with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys of instance's __dict__."""
        dict_rep = {}
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        for k, v in self.__dict__.items():
            dict_rep[k] = v
        return dict_rep
