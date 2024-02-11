#!/usr/bin/python3
"""Simple definition of the State class."""

from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state within the HBnB project."""

    name = ""  # Name of the state
