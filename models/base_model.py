#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.
        If kwargs is not empty, sets each key-value pair in kwargs as
        attribute-value pairs on the instance, except for '__class__'.
        Otherwise, assigns a new uuid and the current datetime to id and
        created_at/updated_at attributes respectively.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance.
        The dictionary includes the class name under the key '__class__'.
        'created_at' and 'updated_at' are converted to string objects in ISO format.
        """
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict
