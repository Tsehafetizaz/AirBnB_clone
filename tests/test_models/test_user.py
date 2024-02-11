#!/usr/bin/python3
"""Unit tests for the User class."""

import unittest
import os
import models
from datetime import datetime
from time import sleep
from models.user import User


class TestUserInstantiation(unittest.TestCase):
    """Tests for User instantiation."""

    def test_no_args_creates_instance(self):
        self.assertIsInstance(User(), User)

    def test_instance_in_storage(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_and_time_attributes(self):
        user = User()
        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)

    def test_user_attributes(self):
        user = User()
        self.assertIsInstance(User.email, str)
        self.assertIsInstance(User.password, str)
        self.assertIsInstance(User.first_name, str)
        self.assertIsInstance(User.last_name, str)

    def test_unique_ids_for_different_instances(self):
        user1, user2 = User(), User()
        self.assertNotEqual(user1.id, user2.id)

    def test_different_time_attributes_for_new_instances(self):
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_string_representation(self):
        user = User()
        user.id = "123"
        str_repr = str(user)
        self.assertIn("[User] (123)", str_repr)

    def test_instantiation_with_kwargs(self):
        dt = datetime.now()
        user = User(
            id="123",
            created_at=dt.isoformat(),
            updated_at=dt.isoformat()
        )
        self.assertEqual(user.id, "123")
        self.assertEqual(user.created_at, dt)
        self.assertEqual(user.updated_at, dt)


class TestUserSave(unittest.TestCase):
    """Tests for the save method of User."""

    @classmethod
    def setUpClass(cls):
        cls.prev_file = "file.json"
        cls.temp_file = "temp.json"
        try:
            os.rename(cls.prev_file, cls.temp_file)
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.rename(cls.temp_file, cls.prev_file)
        except IOError:
            pass

    def test_save_updates_updated_at(self):
        user = User()
        prev_updated_at = user.updated_at
        sleep(0.05)
        user.save()
        self.assertLess(prev_updated_at, user.updated_at)

    def test_save_creates_or_updates_file(self):
        user = User()
        user.save()
        user_id = f"User.{user.id}"
        with open("file.json", "r") as f:
            self.assertIn(user_id, f.read())


class TestUserToDict(unittest.TestCase):
    """Tests for the to_dict method of User."""

    def test_to_dict_returns_correct_keys(self):
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertIsInstance(user_dict["id"], str)
        self.assertIsInstance(user_dict["created_at"], str)
        self.assertIsInstance(user_dict["updated_at"], str)

    def test_to_dict_includes_custom_attrs(self):
        user = User()
        user.name = "Test User"
        user_dict = user.to_dict()
        self.assertIn("name", user_dict)
        self.assertEqual(user_dict["name"], "Test User")


if __name__ == "__main__":
    unittest.main()
