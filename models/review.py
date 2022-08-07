#!/usr/bin/python3
"""Module review.py
that inherits from BaseModel.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """class representing review."""
    place_id = ""
    user_id = ""
    text = ""
