#!/usr/bin/python3
"""Module user.py
that inherits from BaseModel.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """class representing a User."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
