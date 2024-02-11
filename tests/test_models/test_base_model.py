#!/usr/bin/python3
"""
This module contains unittests for the BaseModel class.
"""

import os
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Defines test cases for the BaseModel class.
    """

    def setUp(self):
        """
        Sets up test cases, including renaming the storage file if it exists.
        """
        if os.path.exists("file.json"):
            os.rename("file.json", "tmp.json")

    def tearDown(self):
        """
        Cleans up after tests, restoring the original storage file.
        """
        if os.path.exists("file.json"):
            os.remove("file.json")
        if os.path.exists("tmp.json"):
            os.rename("tmp.json", "file.json")

    def test_init(self):
        """
        Tests the initialization of BaseModel instances.
        """
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        """
        Tests the save method of BaseModel instances.
        """
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

    def test_to_dict(self):
        """
        Tests the to_dict method, ensuring it returns a dictionary with the
        correct keys and formats.
        """
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(
            my_model_dict["created_at"],
            my_model.created_at.isoformat(),
        )
        self.assertEqual(
            my_model_dict["updated_at"],
            my_model.updated_at.isoformat(),
        )

    def test_str(self):
        """
        Tests the string representation of BaseModel instances.
        """
        my_model = BaseModel()
        expected_str = f"[BaseModel] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(str(my_model), expected_str)


if __name__ == "__main__":
    unittest.main()
