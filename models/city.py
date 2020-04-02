#!/usr/bin/python3
"""This is the city class"""
import os
import models
from models.base_model import BaseModel, Base
import models.state
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    This is the class for City. It is linked to the cities table
    Attributes:
        state_id: non-Null String, Foreign Key to State ID associated with city
        name: non-Null String, name of city
    """
    __tablename__ = 'cities'

    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
    if 'HBNB_TYPE_STORAGE' in os.environ:
        if os.environ['HBNB_TYPE_STORAGE'] == 'db':
            # TODO implement the deletion requirement
            places = relationship('Place',
                                  cascade='delete, delete-orphan',
                                  backref='cities')
