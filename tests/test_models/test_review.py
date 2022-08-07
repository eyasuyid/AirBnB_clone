#!/usr/bin/python3
"""Module test_review.py
Tests for class Review.
"""

from models.base_model import BaseModel
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """Tests for class Reiew."""

    def setUp(self):
        pass

    def test_9_4_instatiation(self):
        """Checks for instances."""

        r = Review()
        self.assertEqual(str(type(r)), "<class 'models.review.Review'>")
        self.assertIsInstance(r, Review)
        self.assertTrue(issubclass(Review, BaseModel))

    def test_9_4_class_attr(self):
        """Checks for class attributes."""

        r = Review()
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertTrue(hasattr(Review, "user_id"))
        self.assertTrue(hasattr(Review, "text"))

    def test_9_4_attr(self):
        """Checks for attributes type."""

        r = Review()
        self.assertTrue(r.place_id == "")
        self.assertTrue(r.user_id == "")
        self.assertTrue(r.text == "")

if __name__ == '__main__':
    unittest.main()
