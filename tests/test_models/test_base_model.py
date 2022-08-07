#!/usr/bin/python3
"""Unittest base_model
Test cases for class BaseModel.
"""

import unittest
from datetime import datetime
from uuid import uuid4
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import time
from models import storage


class TestBaseModel(unittest.TestCase):
    """Test case for class BaseModel."""

    def setUp(self):
        """set up test methods."""
        pass

    def teardown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""

        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_3_instance(self):
        """Tests for instance of class BaseModel."""

        b = BaseModel()
        self.assertEqual(str(type(b)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(b, BaseModel)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_3_init_no_args(self):
        """Tests __init__ with no args."""

        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_3_attributes(self):
        """Tests attributes value for instance of class BaseModel."""

        attributes = storage.attributes()["BaseModel"]
        o = BaseModel()
        for k, v, in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

    def test_3_datetime_created_at(self):
        """Tests if created_at is a datetime obj."""

        b = BaseModel()
        self.assertTrue(type(b.created_at) is datetime)

    def test_3_datetime_updated_at(self):
        """Tests if updated_at is a datetime obj."""

        b = BaseModel()
        self.assertTrue(type(b.updated_at) is datetime)

    def test_3_unique_id(self):
        """Checks if instances have unique ids."""

        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_3_id(self):
        """Checks for id"""

        b = BaseModel()
        self.assertTrue(hasattr(b, "id"))

    def test_3_save(self):
        """Tests the public instance method save() updates the updated_at."""

        b = BaseModel()
        b.save()
        self.assertNotEqual(b.created_at, b.updated_at)

    def test_3_str(self):
        """Test for __str__ representation."""

        b = BaseModel()
        self.assertEqual(str(b), "[BaseModel] ({}) {}".format(b.id, b.__dict__))

    def test_3_to_dict(self):
        """Tests for __dict__ public instance."""

        b = BaseModel()
        d = datetime.now()
        b.id = "12345"
        b.created_at = b.updated_at = d
        test_dict = {
            "id": "12345",
            "created_at": d.isoformat(),
            "updated_at": d.isoformat(),
            "__class__": "BaseModel"
            }
        self.assertDictEqual(test_dict, b.to_dict())

    def test_3_to_dict_with_no_args(self):
        """Tests to_dict with no args."""

        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict()
        msg = "to_dict() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)


if __name__ == '__main__':
    unittest.main()
