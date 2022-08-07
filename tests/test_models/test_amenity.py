#!/usr/bin/python3
"""Amenity unittests"""
import unittest
from models.amenity import Amenity
import datetime
import time


class TestAmenity(unittest.TestCase):
    """class TestAmenity"""

    def test_amenity_class_membership_and_attributes(self):
        """Amenity is right class with correct attrs"""
        amenity = Amenity()
        self.assertIsNotNone(amenity.id)
        self.assertIsNotNone(amenity.created_at)
        self.assertIsNotNone(amenity.updated_at)
        self.assertIsInstance(amenity, Amenity)
        self.assertIsNotNone(amenity.name)

    def test_amenity_attr_type(self):
        """Amenity attributes are correct type"""
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)
        self.assertEqual(len(amenity.id), 36)
        self.assertIsInstance(amenity.created_at, datetime.datetime)
        self.assertIsInstance(amenity.updated_at, datetime.datetime)
        self.assertIsInstance(amenity.name, str)

    def test_amenity_updated_at_matches_created_at_initialization(self):
        """Amenity updated_at is same as create_at"""
        amenity = Amenity()
        self.assertEqual(amenity.updated_at, amenity.created_at)

    def test_amenity_str_method(self):
        """Amenity str method creates accurate representation"""
        amenity = Amenity()
        amenity_str = amenity.__str__()
        self.assertIsInstance(amenity_str, str)
        self.assertEqual(amenity_str[:9], '[Amenity]')
        self.assertEqual(amenity_str[10:48], '({})'.format(amenity.id))
        self.assertDictEqual(eval(amenity_str[49:]), amenity.__dict__)

    def test_amenity_save_method(self):
        """Amenity save method alters update_at date"""
        amenity = Amenity()
        time.sleep(0.0001)
        amenity.save()
        self.assertNotEqual(amenity.updated_at, amenity.created_at)

    def test_amenity_to_dict_method(self):
        """Amenity to_dict method creates accurate dictionary"""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['id'], amenity.id)
        self.assertEqual(amenity_dict['__class__'], type(amenity).__name__)
        self.assertEqual(
            amenity_dict['created_at'], amenity.created_at.isoformat())
        self.assertEqual(
            amenity_dict['updated_at'], amenity.updated_at.isoformat())
        self.assertIsInstance(amenity.created_at, datetime.datetime)
        self.assertIsInstance(amenity.updated_at, datetime.datetime)

    def test_amenity_dict_to_instance_with_kwargs(self):
        """Amenity can instantiate new object with dictionary"""
        amenity = Amenity()
        amenity.name = "Betty"
        amenity.number = 972
        amenity_dict = amenity.to_dict()
        new_amenity = Amenity(**amenity_dict)
        new_amenity_dict = new_amenity.to_dict()
        self.assertFalse(new_amenity is amenity)
        self.assertDictEqual(new_amenity_dict, amenity_dict)

    def test_amenity_dict_to_instance_with_empty_kwargs(self):
        """Amenity can instantiate new object with empty dict"""
        amenity_dict = {}
        new_amenity = Amenity(**amenity_dict)
        new_amenity_dict = new_amenity.to_dict()
        self.assertIsInstance(new_amenity, Amenity)
        self.assertIsNotNone(new_amenity.id)
        self.assertIsNotNone(new_amenity.created_at)
        self.assertIsNotNone(new_amenity.updated_at)

if __name__ == '__main__':
    unittest.main()
