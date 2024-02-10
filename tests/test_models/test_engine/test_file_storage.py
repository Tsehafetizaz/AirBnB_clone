import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test suite for the FileStorage class."""

    def setUp(self):
        """Set up method to start each test."""
        self.storage = FileStorage()
        self.file_path = FileStorage._FileStorage__file_path

    def tearDown(self):
        """Tear down method to clean up after tests."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_save_and_reload(self):
        """Test saving to file and reloading."""
        base_model = BaseModel()
        self.storage.new(base_model)
        self.storage.save()
        self.storage.reload()
        key = f"BaseModel.{base_model.id}"
        self.assertIn(key, self.storage.all())
        self.assertIsInstance(self.storage.all()[key], BaseModel)

    def test_all_method(self):
        """Test the all method returns the __objects dictionary."""
        self.assertEqual(self.storage.all(), FileStorage._FileStorage__objects)

    def test_new_method(self):
        """Test new method adds objects correctly to __objects."""
        base_model = BaseModel()
        self.storage.new(base_model)
        key = f"BaseModel.{base_model.id}"
        self.assertIn(key, FileStorage._FileStorage__objects)


if __name__ == '__main__':
    unittest.main()
