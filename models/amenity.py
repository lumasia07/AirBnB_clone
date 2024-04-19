#!/usr/bin/python3
"""Defines a class Amenity"""
import models
from models.base_model import BaseModel, Base
from sqlalhemy.orm import relationship
from os import getenv
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Amenity of BnB

    Args:
        name(str): name of amenity
    """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""
