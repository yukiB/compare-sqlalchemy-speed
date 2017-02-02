# -*- coding: utf-8 -*-

from __future__ import absolute_import, with_statement, print_function, unicode_literals
from sqlalchemy import Table, Column, BigInteger, Unicode, ForeignKey, Integer
from sqlalchemy.orm import mapper
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


from sqlalchemy_test.database import metadata
from sqlalchemy_test.model.base import Base
from sqlalchemy_test.model.team import Team

import time


class User(Base):

    def __repr__(self):
        return '<User %r>' % (self.id)

    def __init__(self, name, age, team):
        self.name = name
        self.age = age
        self.team = team
        self.updated_at = time.time()
        self.created_at = time.time()

    @staticmethod
    def create_dict(name, age, team_id):
        return {'name': name, 'age': age, 'team_id': team_id,
                'updated_at': time.time(), 'created_at': time.time()}


signup_user = Table('user', metadata,
                    Column('id', BigInteger, nullable=False,
                           primary_key=True, autoincrement=True),
                    Column('name', Unicode(255), nullable=False),
                    Column('age', Integer, nullable=False),
                    Column('team_id', ForeignKey('team.id'), nullable=False),
                    Column('updated_at', BigInteger, nullable=False),
                    Column('created_at', BigInteger, nullable=False))

mapper(User, signup_user,
       properties={
           'id': signup_user.c.id,
           'name': signup_user.c.name,
           'age': signup_user.c.age,
           'team': relationship(Team),
           'updated_at': signup_user.c.updated_at,
           'created_at': signup_user.c.created_at
       })

User.__table__ = signup_user


Base = declarative_base()


class UserTable(Base):
    __tablename__ = "user"
    id = Column(BigInteger,  nullable=False,
                primary_key=True, autoincrement=True)
    name = Column(Unicode(255), nullable=False)
    age = Column(Integer, nullable=False)
    team_id = Column(BigInteger, nullable=False)
    updated_at = Column(BigInteger, nullable=False)
    created_at = Column(BigInteger, nullable=False)
