#!/usr/bin/python3
"""Unit tests for the User class."""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_instantiation(self):
        """Test instantiation of User object."""
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(issubclass(type(user), User))
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_attributes(self):
        """Test User specific attributes."""
        user = User()
        user.email = "user@example.com"
        user.password = "password"
        user.first_name = "John"
        user.last_name = "Doe"
        self.assertEqual(user.email, "user@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")


if __name__ == '__main__':
    unittest.main()
