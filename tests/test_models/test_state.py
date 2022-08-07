#!/usr/bin/python3
"""Module test_state.py
Tests for class State.
"""

from models.base_model import BaseModel
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """Tests for class State."""

    def setUp(self):
        pass

    def test_9_1_instatiation(self):
        """Checks for instances."""

        s = State()
        self.assertEqual(str(type(s)), "<class 'models.state.State'>")
        self.assertIsInstance(s, State)
        self.assertTrue(issubclass(State, BaseModel))

    def test_9_1_class_attr(self):
        """Checks for class attributes."""

        s = State()
        self.assertTrue(hasattr(State, "name"))

    def test_9_1_attr(self):
        """Checks for attributes type."""

        s = State()
        self.assertTrue(s.name == "")

if __name__ == '__main__':
    unittest.main()
