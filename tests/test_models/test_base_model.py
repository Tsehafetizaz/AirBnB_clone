#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_init(self):
        """Test initialization of BaseModel instances."""
        instance = BaseModel()
        self.assertTrue(isinstance(instance, BaseModel))
        self.assertTrue(hasattr(instance, "id"))
        self.assertTrue(hasattr(instance, "created_at"))
        self.assertTrue(hasattr(instance, "updated_at"))
        self.assertTrue(isinstance(instance.created_at, datetime))
        self.assertTrue(isinstance(instance.updated_at, datetime))

    def test_str_representation(self):
        """Test the string representation of a BaseModel instance."""
        instance = BaseModel()
        expected = f"[BaseModel] ({instance.id}) {instance.__dict__}"
        self.assertEqual(expected, instance.__str__())

    def test_save(self):
        """Test the save method of the BaseModel class."""
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(old_updated_at, instance.updated_at)

    def test_to_dict(self):
        """Test conversion of BaseModel instance to a dictionary."""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertEqual(instance_dict['id'], instance.id)
        self.assertTrue('created_at' in instance_dict)
        self.assertTrue('updated_at' in instance_dict)
        self.assertTrue(isinstance(instance_dict['created_at'], str))
        self.assertTrue(isinstance(instance_dict['updated_at'], str))


if __name__ == '__main__':
    unittest.main()
