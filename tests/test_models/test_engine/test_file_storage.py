#!/usr/bin/python3
"""Unit tests for FileStorage in models/engine/file_storage.py."""

import unittest
import os
import json
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class TestFileStorageInstantiation(unittest.TestCase):
    """Tests instantiation of FileStorage."""

    def test_no_args_creates_instance(self):
        self.assertIsInstance(FileStorage(), FileStorage)

    def test_no_arg_raises_error(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_path_private(self):
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))

    def test_objects_private(self):
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))

    def test_storage_type(self):
        self.assertIsInstance(models.storage, FileStorage)


class TestFileStorageMethods(unittest.TestCase):
    """Tests methods of FileStorage."""

    @classmethod
    def setUpClass(cls):
        cls.test_file = "file.json"
        try:
            os.rename(cls.test_file, "tmp_test")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove(cls.test_file)
        except IOError:
            pass
        try:
            os.rename("tmp_test", cls.test_file)
        except IOError:
            pass

    def setUp(self):
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        try:
            os.remove(self.test_file)
        except IOError:
            pass

    def test_all_returns_dict(self):
        self.assertIsInstance(models.storage.all(), dict)

    def test_all_no_args(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        bm = BaseModel()
        models.storage.new(bm)
        key = f"BaseModel.{bm.id}"
        self.assertIn(key, models.storage.all())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        bm = BaseModel()
        models.storage.new(bm)
        models.storage.save()
        with open(self.test_file, "r") as f:
            self.assertIn(f"BaseModel.{bm.id}", f.read())

    def test_save_no_args(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        bm = BaseModel()
        models.storage.new(bm)
        models.storage.save()
        models.storage.reload()
        key = f"BaseModel.{bm.id}"
        self.assertIn(key, models.storage.all())

    def test_reload_no_args(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
