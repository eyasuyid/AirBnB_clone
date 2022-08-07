#!/usr/bin/python3
"""Module test_user.py
unittest for User.
"""

from models.base_model import BaseModel
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """class TestUser."""

    def setUp(self):
        pass

    def test_8_instantiation(self):
        """Tests instatiation of User class."""

        u = User()
        self.assertEqual(str(type(u)), "<class 'models.user.User'>")
        self.assertIsInstance(u, User)
        self.assertTrue(issubclass(type(u), BaseModel))

    def test_8_attr_are_class_attrs(self):
        """checks if attributes are of the class attributes."""

        u = User()
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))
        self.assertTrue(hasattr(User, "email"))
        self.assertTrue(hasattr(User, "password"))

    def test_8_attributes(self):

        u = User()
        self.assertTrue(u.first_name == "")
        self.assertTrue(u.last_name == "")
        self.assertIs(type(u.email), str)
        self.assertIs(type(u.password), str)

if __name__ == '__main__':
    unittest.main()
