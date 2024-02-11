#!/usr/bin/python3
"""Unit tests for the BaseModel class."""

import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel
import models


class TestBaseModelInstantiation(unittest.TestCase):
    """Tests for instantiation of BaseModel."""

    def test_no_args_creates_instance(self):
        self.assertIsInstance(BaseModel(), BaseModel)

    def test_instance_in_storage(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertIsInstance(BaseModel().id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(BaseModel().created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(BaseModel().updated_at, datetime)

    def test_unique_ids_for_different_instances(self):
        bm1, bm2 = BaseModel(), BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_different_created_at_for_new_instances(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_different_updated_at_for_new_instances(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_string_representation(self):
        dt = datetime.today()
        bm = BaseModel()
        bm.id = '123456'
        bm.created_at = bm.updated_at = dt
        str_repr = str(bm)
        self.assertIn('[BaseModel] (123456)', str_repr)
        self.assertIn("'id': '123456'", str_repr)
        self.assertIn(f"'created_at': {repr(dt)}", str_repr)
        self.assertIn(f"'updated_at': {repr(dt)}", str_repr)

    def test_unused_args_ignored(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        bm = BaseModel(
            id='345',
            created_at=dt.isoformat(),
            updated_at=dt.isoformat()
        )
        self.assertEqual(bm.id, '345')
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_kwargs_with_None_raises_error(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        bm = BaseModel(
            "12",
            id='345',
            created_at=dt.isoformat(),
            updated_at=dt.isoformat()
        )
        self.assertEqual(bm.id, '345')
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)


class TestBaseModelSave(unittest.TestCase):
    """Tests for the save method of BaseModel."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_single_save(self):
        bm = BaseModel()
        sleep(0.05)
        before_save = bm.updated_at
        bm.save()
        self.assertLess(before_save, bm.updated_at)

    def test_multiple_saves(self):
        bm = BaseModel()
        sleep(0.05)
        first_save = bm.updated_at
        bm.save()
        second_save = bm.updated_at
        self.assertLess(first_save, second_save)
        sleep(0.05)
        bm.save()
        self.assertLess(second_save, bm.updated_at)

    def test_save_with_arg_raises_error(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bm_id = f"BaseModel.{bm.id}"
        with open("file.json", "r") as f:
            self.assertIn(bm_id, f.read())


class TestBaseModelToDict(unittest.TestCase):
    """Tests for to_dict method of BaseModel."""

    def test_to_dict_returns_dict(self):
        self.assertIsInstance(BaseModel().to_dict(), dict)

    def test_to_dict_contains_correct_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_to_dict_includes_custom_attributes(self):
        bm = BaseModel()
        bm.name = "Holberton"
        bm.my_number = 98
        bm_dict = bm.to_dict()
        self.assertIn("name", bm_dict)
        self.assertIn("my_number", bm_dict)

    def test_datetime_attributes_in_dict_as_str(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertIsInstance(bm_dict["created_at"], str)
        self.assertIsInstance(bm_dict["updated_at"], str)

    def test_to_dict_output(self):
        dt = datetime.today()
        bm = BaseModel()
        bm.id = '123456'
        bm.created_at = bm.updated_at = dt
        expected_dict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(bm.to_dict(), expected_dict)

    def test_to_dict_differs_from_dunder_dict(self):
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_with_arg_raises_error(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


if __name__ == "__main__":
    unittest.main()
