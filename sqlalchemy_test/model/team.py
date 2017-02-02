# -*- coding: utf-8 -*-

from __future__ import absolute_import, with_statement, print_function, unicode_literals
from sqlalchemy import Table, Column, BigInteger, Unicode
from sqlalchemy.orm import mapper

from sqlalchemy_test.database import metadata
from sqlalchemy_test.model.base import Base

import time


class Team(Base):

    def __repr__(self):
        return '<Team %r>' % (self.id)

    def __init__(self, name):
        self.name = name
        self.updated_at = time.time()
        self.created_at = time.time()

    @staticmethod
    def create_dict(name):
        return {'name': name, 'updated_at': time.time(), 'created_at': time.time()}

signup_team = Table('team', metadata,
                    Column('id', BigInteger, nullable=False,
                           primary_key=True, autoincrement=True),
                    Column('name', Unicode(45), nullable=False),
                    Column('updated_at', BigInteger, nullable=False),
                    Column('created_at', BigInteger, nullable=False))

mapper(Team, signup_team,
       properties={
           'id': signup_team.c.id,
           'name': signup_team.c.name,
           'updated_at': signup_team.c.updated_at,
           'created_at': signup_team.c.created_at
       })

Team.__table__ = signup_team
