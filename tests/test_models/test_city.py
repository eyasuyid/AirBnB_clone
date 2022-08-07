#!/usr/bin/python3
"""City unittests"""
import unittest
from models.city import City
import datetime
import time


class TestCity(unittest.TestCase):
    """class TestCity"""

    def test_city_class_membership_and_attributes(self):
        """City is right class with correct attrs"""
        city = City()
        self.assertIsNotNone(city.id)
        self.assertIsNotNone(city.created_at)
        self.assertIsNotNone(city.updated_at)
        self.assertIsInstance(city, City)
        self.assertIsNotNone(city.state_id)
        self.assertIsNotNone(city.name)

    def test_city_attr_type(self):
        """City attributes are correct type"""
        city = City()
        self.assertIsInstance(city.id, str)
        self.assertEqual(len(city.id), 36)
        self.assertIsInstance(city.created_at, datetime.datetime)
        self.assertIsInstance(city.updated_at, datetime.datetime)
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

    def test_city_updated_at_matches_created_at_initialization(self):
        """City updated_at is same as create_at"""
        city = City()
        self.assertEqual(city.updated_at, city.created_at)

    def test_city_str_method(self):
        """City str method creates accurate representation"""
        city = City()
        city_str = city.__str__()
        self.assertIsInstance(city_str, str)
        self.assertEqual(city_str[:6], '[City]')
        self.assertEqual(city_str[7:45], '({})'.format(city.id))
        self.assertDictEqual(eval(city_str[46:]), city.__dict__)

    def test_city_save_method(self):
        """City save method alters update_at date"""
        city = City()
        time.sleep(0.0001)
        city.save()
        self.assertNotEqual(city.updated_at, city.created_at)

    def test_city_to_dict_method(self):
        """City to_dict method creates accurate dictionary"""
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['id'], city.id)
        self.assertEqual(city_dict['__class__'], type(city).__name__)
        self.assertEqual(city_dict['created_at'], city.created_at.isoformat())
        self.assertEqual(city_dict['updated_at'], city.updated_at.isoformat())
        self.assertIsInstance(city.created_at, datetime.datetime)
        self.assertIsInstance(city.updated_at, datetime.datetime)

    def test_city_dict_to_instance_with_kwargs(self):
        """City can instantiate new object with dictionary"""
        city = City()
        city.name = "Betty"
        city.number = 972
        city_dict = city.to_dict()
        new_city = City(**city_dict)
        new_city_dict = new_city.to_dict()
        self.assertFalse(new_city is city)
        self.assertDictEqual(new_city_dict, city_dict)

    def test_city_dict_to_instance_with_empty_kwargs(self):
        """City can instantiate new object with empty dict"""
        city_dict = {}
        new_city = City(**city_dict)
        new_city_dict = new_city.to_dict()
        self.assertIsInstance(new_city, City)
        self.assertIsNotNone(new_city.id)
        self.assertIsNotNone(new_city.created_at)
        self.assertIsNotNone(new_city.updated_at)

if __name__ == '__main__':
    unittest.main()
