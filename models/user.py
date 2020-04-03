#!/usr/bin/python3
"""This is the user class"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref


class User(BaseModel, Base):
    """
    This is the class for User objects.
    It is associated with the SQL table 'users'.
    Attributes:
        email: non-Null String, 128 characters
        password: non-Null String, 128 characters
        first_name: nullable String, 128 characters
        last_name: nullable String, 128 characters
    """
    __tablename__ = 'users'

    email = Column(String(128),
                   nullable=False)
    password = Column(String(128),
                      nullable=False)
    first_name = Column(String(128),
                        nullable=True)
    last_name = Column(String(128),
                       nullable=True)

    if 'HBNB_TYPE_STORAGE' in os.environ:
        if os.environ['HBNB_TYPE_STORAGE'] == 'db':
            places = relationship('Place',
                                  backref='user',
                                  cascade='all, delete')
            reviews = relationship('Review',
                                   backref='user',
                                   cascade='all, delete')
