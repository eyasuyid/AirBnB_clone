#!/usr/bin/python3
"""Module test_place.py
Tests for class Place.
"""

from models.base_model import BaseModel
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """Tests for class Place."""

    def setUp(self):
        pass

    def test_9_5_instatiation(self):
        """Checks for instatiation."""

        p = Place()
        self.assertEqual(str(type(p)), "<class 'models.place.Place'>")
        self.assertIsInstance(p, Place)
        self.assertTrue(issubclass(Place, BaseModel))

    def test_9_5_class_attr(self):
        """Checks for class attributes."""

        p = Place()
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertTrue(hasattr(Place, "name"))
        self.assertTrue(hasattr(Place, "description"))
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertTrue(hasattr(Place, "amenity_ids"))

    def test_9_5_attr(self):
        """Checks for attributes type."""

        p = Place()
        self.assertTrue(p.city_id == "")
        self.assertTrue(p.user_id == "")
        self.assertTrue(p.name == "")
        self.assertTrue(p.description == "")
        self.assertTrue(p.number_rooms == 0)
        self.assertTrue(p.number_bathrooms == 0)
        self.assertTrue(p.max_guest == 0)
        self.assertTrue(p.price_by_night == 0)
        self.assertTrue(p.latitude == 0.0)
        self.assertTrue(p.longitude == 0.0)
        self.assertTrue(p.amenity_ids == [])

if __name__ == '__main__':
    unittest.main()
