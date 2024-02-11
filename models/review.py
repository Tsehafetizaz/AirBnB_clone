#!/usr/bin/python3
"""Review class for the HBnB project."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Defines a review for a place."""

    place_id = ""  # ID of the related place
    user_id = ""  # ID of the reviewing user
    text = ""  # Content of the review
