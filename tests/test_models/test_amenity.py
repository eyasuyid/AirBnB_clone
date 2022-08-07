#!/usr/bin/python3
"""Module amenity.py
Test for class Amenity.
"""

from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """Tests for class Amenity."""

    def setUp(self):
        pass

    def test_9_3_instatiation(self):
        """Checks for instances."""

        a = Amenity()
        self.assertEqual(str(type(a)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(a, Amenity)
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_9_3_class_attr(self):
        """Checks for class attributes."""

        a = Amenity()
        self.assertTrue(hasattr(Amenity, "name"))

    def test_9_3_attr(self):
        """Checks for attributes type."""

        a = Amenity()
        self.assertTrue(a.name == "")

if __name__ == '__main__':
    unittest.main()
