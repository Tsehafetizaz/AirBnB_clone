#!/usr/bin/python3
"""Unit tests for the State class."""

import unittest
import models
from datetime import datetime
from time import sleep
from models.state import State


class TestStateInstantiation(unittest.TestCase):
    """Tests for State instantiation."""

    def test_no_args_creates_instance(self):
        self.assertIsInstance(State(), State)

    def test_instance_in_storage(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_and_time_attributes(self):
        state = State()
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)

    def test_name_attribute(self):
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertIsInstance(State.name, str)

    def test_unique_ids_for_instances(self):
        state1, state2 = State(), State()
        self.assertNotEqual(state1.id, state2.id)

    def test_different_time_attributes(self):
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertLess(state1.created_at, state2.created_at)
        self.assertLess(state1.updated_at, state2.updated_at)

    def test_string_representation(self):
        state = State()
        state.id = "123"
        str_repr = str(state)
        self.assertIn("[State] (123)", str_repr)

    def test_instantiation_with_kwargs(self):
        dt = datetime.now()
        state = State(
            id="123",
            created_at=dt.isoformat(),
            updated_at=dt.isoformat()
        )
        self.assertEqual(state.id, "123")
        self.assertEqual(state.created_at, dt)
        self.assertEqual(state.updated_at, dt)


class TestStateSave(unittest.TestCase):
    """Tests for State's save method."""

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
        state = State()
        prev_updated_at = state.updated_at
        sleep(0.05)
        state.save()
        self.assertLess(prev_updated_at, state.updated_at)

    def test_save_creates_or_updates_file(self):
        state = State()
        state.save()
        state_id = f"State.{state.id}"
        with open("file.json", "r") as f:
            self.assertIn(state_id, f.read())


class TestStateToDict(unittest.TestCase):
    """Tests for State's to_dict method."""

    def test_to_dict_returns_correct_keys(self):
        state = State()
        state_dict = state.to_dict()
        self.assertEqual(state_dict["__class__"], "State")
        self.assertIsInstance(state_dict["id"], str)
        self.assertIsInstance(state_dict["created_at"], str)
        self.assertIsInstance(state_dict["updated_at"], str)

    def test_to_dict_includes_custom_attrs(self):
        state = State()
        state.name = "Test State"
        state_dict = state.to_dict()
        self.assertIn("name", state_dict)
        self.assertEqual(state_dict["name"], "Test State")


if __name__ == "__main__":
    unittest.main()
