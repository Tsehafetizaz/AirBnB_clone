#!/usr/bin/python3
"""Simple definition of the User class."""

from models.base_model import BaseModel


class User(BaseModel):
    """Defines a user for the HBnB project."""

    email = ""  # Email address of the user
    password = ""  # Password of the user
    first_name = ""  # First name of the user
    last_name = ""  # Last name of the user
