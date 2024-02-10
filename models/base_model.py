#!/usr/bin/python3
"""Module for BaseModel class."""

import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes.

    Attributes:
        id (str): Unique id for each instance, assigned with an UUID.
        created_at (datetime): Datetime when an instance is created.
        updated_at (datetime): Datetime when an instance is updated.
    """

    def __init__(self):
        """Initializes the BaseModel instance."""
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the instance's 'updated_at' attribute current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values instance __dict__.

        Includes the class name under the key '__class__'. The 'created_at'
        'updated_at' datetime objects are converted to strings in ISO format.
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
