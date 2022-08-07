#!/usr/bin/python3
"""Place unittests"""
import unittest
from models.place import Place
import datetime
import time


class TestPlace(unittest.TestCase):
    """class TestPlace"""

    def test_place_class_membership_and_attributes(self):
        """Place is right class with correct attrs"""
        place = Place()
        self.assertIsNotNone(place.id)
        self.assertIsNotNone(place.created_at)
        self.assertIsNotNone(place.updated_at)
        self.assertIsInstance(place, Place)
        self.assertIsNotNone(place.city_id)
        self.assertIsNotNone(place.user_id)
        self.assertIsNotNone(place.name)
        self.assertIsNotNone(place.description)
        self.assertIsNotNone(place.number_rooms)
        self.assertIsNotNone(place.number_bathrooms)
        self.assertIsNotNone(place.max_guest)
        self.assertIsNotNone(place.price_by_night)
        self.assertIsNotNone(place.latitude)
        self.assertIsNotNone(place.longitude)
        self.assertIsNotNone(place.amenity_ids)

    def test_place_attr_type(self):
        """Place attributes are correct type"""
        place = Place()
        self.assertIsInstance(place.id, str)
        self.assertEqual(len(place.id), 36)
        self.assertIsInstance(place.created_at, datetime.datetime)
        self.assertIsInstance(place.updated_at, datetime.datetime)
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)

    def test_place_updated_at_matches_created_at_initialization(self):
        """Place updated_at is same as create_at"""
        place = Place()
        self.assertEqual(place.updated_at, place.created_at)

    def test_place_str_method(self):
        """Place str method creates accurate representation"""
        place = Place()
        place_str = place.__str__()
        self.assertIsInstance(place_str, str)
        self.assertEqual(place_str[:7], '[Place]')
        self.assertEqual(place_str[8:46], '({})'.format(place.id))
        self.assertDictEqual(eval(place_str[47:]), place.__dict__)

    def test_place_save_method(self):
        """Place save method alters update_at date"""
        place = Place()
        time.sleep(0.0001)
        place.save()
        self.assertNotEqual(place.updated_at, place.created_at)

    def test_place_to_dict_method(self):
        """Place to_dict method creates accurate dictionary"""
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['id'], place.id)
        self.assertEqual(place_dict['__class__'], type(place).__name__)
        self.assertEqual(
            place_dict['created_at'], place.created_at.isoformat())
        self.assertEqual(
            place_dict['updated_at'], place.updated_at.isoformat())
        self.assertIsInstance(place.created_at, datetime.datetime)
        self.assertIsInstance(place.updated_at, datetime.datetime)

    def test_place_dict_to_instance_with_kwargs(self):
        """Place can instantiate new object with dictionary"""
        place = Place()
        place.name = "Betty"
        place.number = 972
        place_dict = place.to_dict()
        new_place = Place(**place_dict)
        new_place_dict = new_place.to_dict()
        self.assertFalse(new_place is place)
        self.assertDictEqual(new_place_dict, place_dict)

    def test_place_dict_to_instance_with_empty_kwargs(self):
        """Place can instantiate new object with empty dict"""
        place_dict = {}
        new_place = Place(**place_dict)
        new_place_dict = new_place.to_dict()
        self.assertIsInstance(new_place, Place)
        self.assertIsNotNone(new_place.id)
        self.assertIsNotNone(new_place.created_at)
        self.assertIsNotNone(new_place.updated_at)

if __name__ == '__main__':
    unittest.main()
