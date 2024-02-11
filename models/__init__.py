#!/usr/bin/python3
"""This module turns models into a Python package."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
