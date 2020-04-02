#!/usr/bin/python3
"""This is the amenity class"""
# import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    This is the class for Amenity objects.
    It is associated with the SQL table 'amenities'.
    Attributes:
        name: non-Null String, 128 characters
    """
    __tablename__ = 'amenities'

    name = Column(String(128),
                  nullable=False)
    place_amenities = relationship('Place',
                                   secondary='place_amenity')
