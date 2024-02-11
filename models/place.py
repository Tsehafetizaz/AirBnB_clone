#!/usr/bin/python3
"""Simple definition of the Place class."""

from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a place for HBnB project."""

    city_id = ""  # ID of the city where the place is located
    user_id = ""  # ID of the user that owns the place
    name = ""  # Name of the place
    description = ""  # Description of the place
    number_rooms = 0  # Number of rooms in the place
    number_bathrooms = 0  # Number of bathrooms in the place
    max_guest = 0  # Maximum number of guests the place can accommodate
    price_by_night = 0  # Price per night to rent the place
    latitude = 0.0  # Latitude of the place
    longitude = 0.0  # Longitude of the place
    amenity_ids = []  # List of amenity IDs associated with the place
