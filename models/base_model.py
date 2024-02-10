#!/usr/bin/python3
"""BaseModel class module."""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initializes the BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ('created_at', 'updated_at'):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """Updates 'updated_at' and saves to file storage."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys instance's __dict__."""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
