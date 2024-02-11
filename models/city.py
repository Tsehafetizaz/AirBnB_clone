#!/usr/bin/python3
"""City class definition."""

from models.base_model import BaseModel


class City(BaseModel):
    """Defines a city with related attributes."""

    state_id = ""  # Identifier for the state
    name = ""  # Name of the city
