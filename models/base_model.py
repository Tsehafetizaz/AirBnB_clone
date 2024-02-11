#!/usr/bin/env python3
"""BaseModel class for Flask applications."""
import uuid
from datetime import datetime


class BaseModel:
    """Base class for all models."""

    def __init__(self):
        """Initializes the BaseModel instance."""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Returns a string representation of the instance."""
        return (f"[{self.__class__.__name__}: {self.id}] - "
                f"{self.created_at:%Y-%m-%d %H:%M:%S}")

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict


if __name__ == "__main__":
    # You can include code here to test the BaseModel class, but make sure
    # to remove it when using this class in an actual Flask application.
    pass
