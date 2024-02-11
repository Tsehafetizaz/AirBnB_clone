#!/usr/bin/python3
"""Unit tests for the Review class."""

import os
import unittest
from datetime import datetime
from time import sleep
from models.review import Review
import models


class TestReviewInstantiation(unittest.TestCase):
    """Tests for instantiation of Review objects."""

    def test_no_args_creates_instance(self):
        self.assertIsInstance(Review(), Review)

    def test_instance_in_storage(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertIsInstance(Review().id, str)

    def test_created_at_and_updated_at_are_datetimes(self):
        review = Review()
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)

    def test_public_class_attributes(self):
        review = Review()
        self.assertIsInstance(Review.place_id, str)
        self.assertIsInstance(Review.user_id, str)
        self.assertIsInstance(Review.text, str)

    def test_unique_ids_for_different_instances(self):
        review1, review2 = Review(), Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_time_attributes_for_different_instances(self):
        review1 = Review()
        sleep(0.05)
        review2 = Review()
        self.assertLess(review1.created_at, review2.created_at)
        self.assertLess(review1.updated_at, review2.updated_at)

    def test_string_representation(self):
        review = Review()
        review.id = "123abc"
        str_repr = str(review)
        self.assertIn("[Review] (123abc)", str_repr)

    def test_instantiation_with_kwargs(self):
        dt = datetime.now()
        review = Review(
            id="123",
            created_at=dt.isoformat(),
            updated_at=dt.isoformat()
        )
        self.assertEqual(review.id, "123")
        self.assertEqual(review.created_at, dt)
        self.assertEqual(review.updated_at, dt)


class TestReviewSave(unittest.TestCase):
    """Tests for the save method of Review objects."""

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
            os.remove(cls.prev_file)
        except IOError:
            pass
        try:
            os.rename(cls.temp_file, cls.prev_file)
        except IOError:
            pass

    def test_save_updates_updated_at(self):
        review = Review()
        prev_updated_at = review.updated_at
        sleep(0.05)
        review.save()
        self.assertLess(prev_updated_at, review.updated_at)

    def test_save_creates_or_updates_file(self):
        review = Review()
        review.save()
        review_id = f"Review.{review.id}"
        with open("file.json", "r") as f:
            self.assertIn(review_id, f.read())


class TestReviewToDict(unittest.TestCase):
    """Tests for the to_dict method of Review objects."""

    def test_to_dict_contains_correct_keys_and_data_types(self):
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertEqual(type(review_dict["id"]), str)
        self.assertEqual(type(review_dict["created_at"]), str)
        self.assertEqual(type(review_dict["updated_at"]), str)

    def test_to_dict_includes_custom_attributes(self):
        review = Review()
        review.name = "Test Review"
        review_dict = review.to_dict()
        self.assertIn("name", review_dict)
        self.assertEqual(review_dict["name"], "Test Review")


if __name__ == "__main__":
    unittest.main()
