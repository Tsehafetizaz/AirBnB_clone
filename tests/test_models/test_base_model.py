#!/usr/bin/python3
"""Unit tests for the BaseModel class."""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Defines test cases for the BaseModel class functionality."""

    def test_init(self):
        """Test case for correct initialization of BaseModel instances."""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))

    def test_str(self):
        """Test case for the __str__ method of BaseModel."""
        model = BaseModel()
        expected_str_format = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(model.__str__(), expected_str_format)

    def test_save(self):
        """Test case for the 'save' method of BaseModel."""
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, original_updated_at)

    def test_to_dict(self):
        """Test case for the 'to_dict' method of BaseModel."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertIn('id', model_dict)


if __name__ == "__main__":
    unittest.main()
