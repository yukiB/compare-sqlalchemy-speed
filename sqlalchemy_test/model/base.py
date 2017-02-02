# -*- coding: utf-8 -*-

from __future__ import absolute_import, with_statement, print_function, unicode_literals
import sqlalchemy_test.database as database


class Base(object):

    def __iter__(self):
        return iter(self.__dict__.items())

    def dict(self):
        return self.__dict__

    @classmethod
    def query(cls):
        if not hasattr(cls, "_query"):
            cls._query = database.session().query_property()
        return cls._query
