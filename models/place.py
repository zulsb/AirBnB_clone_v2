#!/usr/bin/python3
"""This is the place class"""
import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from models.amenity import Amenity
from models.review import Review
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'

    city_id = Column(String(60),
                     ForeignKey('cities.id'),
                     nullable=False)
    user_id = Column(String(60),
                     ForeignKey('users.id'),
                     nullable=False)
    name = Column(String(128),
                  nullable=False)
    description = Column(String(1024),
                         nullable=True)
    number_rooms = Column(Integer,
                          nullable=False,
                          default=0)
    number_bathrooms = Column(Integer,
                              nullable=False,
                              default=0)
    max_guest = Column(Integer,
                       nullable=False,
                       default=0)
    price_by_night = Column(Integer,
                            nullable=False,
                            default=0)
    latitude = Column(Float,
                      nullable=True)
    longitude = Column(Float,
                       nullable=True)
    amenity_ids = []

    if 'HBNB_TYPE_STORAGE' in os.environ:
        if os.environ['HBNB_TYPE_STORAGE'] == 'db':
            # TODO implement the deletion requirement
            reviews = relationship('Review',
                                   cascade='delete, delete-orphan',
                                   backref='place')
            amenities = relationship('Amenity',
                                     secondary='place_amenity')
    else:
        @property
        def reviews(self):
            """Property getter of list of Review instances
            where place_id equals current Place.id"""
            review_dict = storage.all(Review)
            return [review for review in review_dict.values()
                    if review.place_id == self.id]

        @property
        def amenities(self):
            """Property getter of list of Amenity instances
            where place_id equals current Place.id"""
            amenity_dict = storage.all(Amenity)
            return [amenity for amenity in amenity_dict.values()
                    if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, amty):
            """Property setter that appends `amty`'s id
            to the current Place amenity_ids"""
            if isinstance(amty, Amenity) and amty.id not in self.amenity_ids:
                self.amenity_ids.append(amty.id)
