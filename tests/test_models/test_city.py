#!/usr/bin/python3
"""Module test_city.py
Tests for class City.
"""


from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """Tests for class City."""

    def setUp(self):
        pass

    def test_9_2_instatiation(self):
        """Test for instances."""

        c = City()
        self.assertEqual(str(type(c)), "<class 'models.city.City'>")
        self.assertIsInstance(c, City)
        self.assertTrue(issubclass(City, BaseModel))

    def test_9_2_class_attr(self):
        """Checks for class attributes."""

        c = City()
        self.assertTrue(hasattr(City, "state_id"))
        self.assertTrue(hasattr(City, "name"))

    def test_9_2_attr(self):
        """Checks for attributes types."""
        c = City()
        self.assertTrue(c.state_id == "")
        self.assertTrue(c.name == "")

if __name__ == '__main__':
    unittest.main()
