#!/usr/bin/python3
"""This is the state class"""
import os
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship, backref


class State(BaseModel, Base):
    """
    This is the class for State objects.
    It is associated with the SQL table 'states'.
    Attributes:
        name: String, 128 characters
    """
    if os.getenv('HBNB_TYPE_STORAGE') == 'file':
        @property
        def cities(self):
            '''returns the list of City instances with
            state_id equals to the current State.id'''
            all_cities = models.storage.all(City)
            cities_in_state = []
            for city in all_cities.values():
                if city.state_id == self.id:
                    cities_in_state.append(city)
            return cities_in_state
    elif os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")
