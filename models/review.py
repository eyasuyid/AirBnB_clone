#!/usr/bin/python3
"""Review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class Review
    Attributes:
        place_id (str): Place ID.
        user_id (str): User ID.
        text (str): Text.
    """
    place_id = ""
    user_id = ""
    text = ""
