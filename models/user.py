#!/usr/bin/python3
"""This is the user class"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref


class User(BaseModel, Base): 
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    if 'HBNB_TYPE_STORAGE' in os.environ:
        if os.environ['HBNB_TYPE_STORAGE'] == 'db':
            # TODO implement the deletion requirement
            places = relationship('Place',
                                  cascade='delete, delete-orphan',
                                  backref='user')
            reviews = relationship('Review',
                                   cascade='delete, delete-orphan',
                                   backref='user')
