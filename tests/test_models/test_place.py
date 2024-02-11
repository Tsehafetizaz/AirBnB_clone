#!/usr/bin/python3
"""Unit tests for the Place class from models.place.py."""

import unittest
import models
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlaceInstantiation(unittest.TestCase):
    """Test the instantiation of Place objects."""

    def test_no_args_creates_instance(self):
        self.assertIsInstance(Place(), Place)

    def test_instance_in_storage(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertIsInstance(Place().id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(Place().created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(Place().updated_at, datetime)

    def test_public_class_attributes(self):
        place = Place()
        self.assertIsInstance(Place.city_id, str)
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertIsInstance(Place.user_id, str)
        self.assertTrue(hasattr(place, 'user_id'))
        # Continue for other attributes...

    def test_unique_ids_for_different_instances(self):
        place1, place2 = Place(), Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_different_created_at_for_new_instances(self):
        place1 = Place()
        sleep(0.05)
        place2 = Place()
        self.assertLess(place1.created_at, place2.created_at)

    def test_different_updated_at_for_new_instances(self):
        place1 = Place()
        sleep(0.05)
        place2 = Place()
        self.assertLess(place1.updated_at, place2.updated_at)

    def test_string_representation(self):
        dt = datetime.today()
        place = Place()
        place.id = "123456"
        place.created_at = place.updated_at = dt
        str_repr = str(place)
        self.assertIn("[Place] (123456)", str_repr)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        place = Place(
            id="345",
            created_at=dt.isoformat(),
            updated_at=dt.isoformat()
        )
        self.assertEqual(place.id, "345")
        self.assertEqual(place.created_at, dt)
        self.assertEqual(place.updated_at, dt)

    def test_instantiation_with_None_kwargs_raises_error(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlaceSave(unittest.TestCase):
    """Test the save method of Place objects."""

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

    def test_one_save_updates_updated_at(self):
        place = Place()
        sleep(0.05)
        before_save = place.updated_at
        place.save()
        self.assertLess(before_save, place.updated_at)

    def test_save_updates_file(self):
        place = Place()
        place.save()
        place_id = f"Place.{place.id}"
        with open("file.json", "r") as f:
            self.assertIn(place_id, f.read())


class TestPlaceToDict(unittest.TestCase):
    """Test the to_dict method of Place objects."""

    def test_to_dict_returns_dict(self):
        self.assertIsInstance(Place().to_dict(), dict)

    def test_to_dict_contains_correct_keys(self):
        place = Place()
        self.assertIn("id", place.to_dict())
        self.assertIn("created_at", place.to_dict())
        self.assertIn("updated_at", place.to_dict())
        self.assertIn("__class__", place.to_dict())

    def test_to_dict_includes_custom_attributes(self):
        place = Place()
        place.middle_name = "Holberton"
        place.my_number = 98
        place_dict = place.to_dict()
        self.assertIn("middle_name", place_dict)
        self.assertIn("my_number", place_dict)

    def test_to_dict_output(self):
        dt = datetime.today()
        place = Place()
        place.id = "123456"
        place.created_at = place.updated_at = dt
        expected_dict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(place.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
