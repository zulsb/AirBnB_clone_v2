#!/usr/bin/python3
"""This is the state class"""
import os
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship, backref


class State(BaseModel, Base):
    """This is the class for State objects.
    Attributes:
        name: Input name.
    """
    __tablename__ = "states"
    name = Column(String(128),
                  nullable=False)

    if "HBNB_TYPE_STORAGE" in os.environ:
        if os.environ["HBNB_TYPE_STORAGE"] == "db":
            cities = relationship("City",
                                  backref="state",
                                  cascade="all, delete")
        elif os.environ["HBNB_TYPE_STORAGE"] == "fs":
            @property
            def cities(self):
                """Property getter of list of city instances
                where state_id equals current State.id"""
                city_dict = models.storage.all(City)
                return [city for city in city_dict.values()
                        if city.state_id == self.id]
