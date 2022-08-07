#!/usr/bin/python3
"""City module"""
from models.base_model import BaseModel


class City(BaseModel):
    """class City
    Attributes:
        state_id (str) State ID.
        name (str): City name.
    """
    state_id = ""
    name = ""
