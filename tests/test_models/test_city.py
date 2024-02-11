#!/usr/bin/python3
"""Unit tests for the City class in models/city.py."""

import unittest
import models
from datetime import datetime
from time import sleep
from models.city import City


class TestCityInstantiation(unittest.TestCase):
    """Test cases for the instantiation of City objects."""

    def test_no_args_creates_instance(self):
        self.assertIsInstance(City(), City)

    def test_instance_in_storage(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertIsInstance(City().id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(City().created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(City().updated_at, datetime)

    def test_state_id_is_class_attribute(self):
        self.assertIsInstance(City.state_id, str)
        self.assertTrue(hasattr(City(), 'state_id'))

    def test_name_is_class_attribute(self):
        self.assertIsInstance(City.name, str)
        self.assertTrue(hasattr(City(), 'name'))

    def test_unique_ids_for_different_instances(self):
        city1, city2 = City(), City()
        self.assertNotEqual(city1.id, city2.id)

    def test_different_created_at_for_new_instances(self):
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.created_at, city2.created_at)

    def test_different_updated_at_for_new_instances(self):
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.updated_at, city2.updated_at)

    def test_string_representation(self):
        dt = datetime.today()
        city = City()
        city.id = "123456"
        city.created_at = city.updated_at = dt
        str_repr = str(city)
        self.assertIn("[City] (123456)", str_repr)

    def test_unused_args_ignored(self):
        city = City(None)
        self.assertNotIn(None, city.__dict__)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        city = City(
            id="345",
            created_at=dt.isoformat(),
            updated_at=dt.isoformat()
        )
        self.assertEqual(city.id, "345")
        self.assertEqual(city.created_at, dt)
        self.assertEqual(city.updated_at, dt)

    def test_instantiation_with_None_kwargs_raises_error(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCitySave(unittest.TestCase):
    """Test cases for the save method of City objects."""

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
        city = City()
        sleep(0.05)
        before_save = city.updated_at
        city.save()
        self.assertLess(before_save, city.updated_at)

    def test_multiple_saves_update_updated_at(self):
        city = City()
        sleep(0.05)
        first_save = city.updated_at
        city.save()
        second_save = city.updated_at
        self.assertLess(first_save, second_save)
        sleep(0.05)
        city.save()
        self.assertLess(second_save, city.updated_at)

    def test_save_with_arg_raises_error(self):
        city = City()
        with self.assertRaises(TypeError):
            city.save(None)

    def test_save_updates_file(self):
        city = City()
        city.save()
        city_id = "City." + city.id
        with open("file.json", "r") as f:
            self.assertIn(city_id, f.read())


class TestCityToDict(unittest.TestCase):
    """Test cases for the to_dict method of City objects."""

    def test_to_dict_returns_dict(self):
        self.assertIsInstance(City().to_dict(), dict)

    def test_to_dict_contains_correct_keys(self):
        city = City()
        self.assertIn("id", city.to_dict())
        self.assertIn("created_at", city.to_dict())
        self.assertIn("updated_at", city.to_dict())
        self.assertIn("__class__", city.to_dict())

    def test_to_dict_includes_custom_attributes(self):
        city = City()
        city.middle_name = "Holberton"
        city.my_number = 98
        city_dict = city.to_dict()
        self.assertIn("middle_name", city_dict)
        self.assertIn("my_number", city_dict)

    def test_datetime_attributes_in_dict_as_str(self):
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict["created_at"], str)
        self.assertIsInstance(city_dict["updated_at"], str)

    def test_to_dict_output(self):
        dt = datetime.today()
        city = City()
        city.id = "123456"
        city.created_at = city.updated_at = dt
        expected_dict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(city.to_dict(), expected_dict)

    def test_to_dict_differs_from_dunder_dict(self):
        city = City()
        self.assertNotEqual(city.to_dict(), city.__dict__)

    def test_to_dict_with_arg_raises_error(self):
        city = City()
        with self.assertRaises(TypeError):
            city.to_dict(None)


if __name__ == "__main__":
    unittest.main()
