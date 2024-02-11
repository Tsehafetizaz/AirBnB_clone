#!/usr/bin/python3
import sys
import os
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class."""

    def test_base_model_instance(self):
        """Test creation of a BaseModel instance."""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

    def test_base_model_attributes(self):
        """Test BaseModel attributes."""
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

    def test_str_method(self):
        """Test the __str__ method of BaseModel."""
        my_model = BaseModel()
        expected_str = f"[BaseModel] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(str(my_model), expected_str)

    def test_save_method(self):
        """Test the save method of BaseModel."""
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method of BaseModel."""
        my_model = BaseModel()
        self.assertIsInstance(my_model.to_dict(), dict)


if __name__ == "__main__":
    unittest.main()
