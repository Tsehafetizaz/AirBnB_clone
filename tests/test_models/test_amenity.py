#!/usr/bin/python3
"""Unit tests for the Amenity class."""

import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity
import models


class TestAmenityInstantiation(unittest.TestCase):
    """Tests instantiation of Amenity class."""

    def test_no_args_creates_instance(self):
        self.assertIsInstance(Amenity(), Amenity)

    def test_instance_in_storage(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertIsInstance(Amenity().id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(Amenity().created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(Amenity().updated_at, datetime)

    def test_name_is_public_attribute(self):
        am = Amenity()
        self.assertIsInstance(Amenity.name, str)
        self.assertTrue(hasattr(am, 'name'))
        self.assertFalse('name' in am.__dict__)

    def test_unique_ids_for_different_instances(self):
        am1, am2 = Amenity(), Amenity()
        self.assertNotEqual(am1.id, am2.id)

    def test_different_created_at_for_new_instances(self):
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.created_at, am2.created_at)

    def test_different_updated_at_for_new_instances(self):
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.updated_at, am2.updated_at)

    def test_string_representation(self):
        dt = datetime.today()
        am = Amenity()
        am.id = '123456'
        am.created_at = am.updated_at = dt
        str_repr = str(am)
        self.assertIn('[Amenity] (123456)', str_repr)
        self.assertIn("'id': '123456'", str_repr)
        self.assertIn("'created_at': {}".format(repr(dt)), str_repr)
        self.assertIn("'updated_at': {}".format(repr(dt)), str_repr)

    def test_unused_args_ignored(self):
        am = Amenity(None)
        self.assertNotIn(None, am.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        am = Amenity(
            id='345',
            created_at=dt.isoformat(),
            updated_at=dt.isoformat()
        )
    self.assertEqual(am.id, '345')
    self.assertEqual(am.created_at, dt)
    self.assertEqual(am.updated_at, dt)

    def test_kwargs_with_None_raises_error(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenitySave(unittest.TestCase):
    """Tests the save method of Amenity class."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_single_save(self):
        am = Amenity()
        sleep(0.05)
        before_save = am.updated_at
        am.save()
        self.assertLess(before_save, am.updated_at)

    def test_multiple_saves(self):
        am = Amenity()
        sleep(0.05)
        first_save = am.updated_at
        am.save()
        second_save = am.updated_at
        self.assertLess(first_save, second_save)
        sleep(0.05)
        am.save()
        self.assertLess(second_save, am.updated_at)

    def test_save_with_arg_raises_error(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.save(None)

    def test_save_updates_file(self):
        am = Amenity()
        am.save()
        am_id = "Amenity." + am.id
        with open("file.json", "r") as f:
            self.assertIn(am_id, f.read())


class TestAmenityToDict(unittest.TestCase):
    """Tests to_dict method of Amenity class."""

    def test_to_dict_returns_dict(self):
        self.assertIsInstance(Amenity().to_dict(), dict)

    def test_to_dict_contains_correct_keys(self):
        am = Amenity()
        self.assertIn('id', am.to_dict())
        self.assertIn('created_at', am.to_dict())
        self.assertIn('updated_at', am.to_dict())
        self.assertIn('__class__', am.to_dict())

    def test_to_dict_includes_custom_attributes(self):
        am = Amenity()
        am.middle_name = "Holberton"
        am.my_number = 98
        am_dict = am.to_dict()
        self.assertIn('middle_name', am_dict)
        self.assertIn('my_number', am_dict)

    def test_to_dict_datetime_attributes_as_str(self):
        am = Amenity()
        am_dict = am.to_dict()
        self.assertIsInstance(am_dict['created_at'], str)
        self.assertIsInstance(am_dict['updated_at'], str)

    def test_to_dict_output(self):
        dt = datetime.today()
        am = Amenity()
        am.id = '123456'
        am.created_at = am.updated_at = dt
        expected_dict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(am.to_dict(), expected_dict)

    def test_to_dict_differs_from_dunder_dict(self):
        am = Amenity()
        self.assertNotEqual(am.to_dict(), am.__dict__)

    def test_to_dict_with_arg_raises_error(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.to_dict(None)


if __name__ == "__main__":
    unittest.main()
