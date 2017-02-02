# -*- coding: utf-8 -*-

from __future__ import absolute_import, with_statement, print_function, unicode_literals
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

_engine = None

_session = None

metadata = MetaData()


def create_local_session():
    global _engine
    session = sessionmaker(autocommit=False,
                           autoflush=True,
                           expire_on_commit=False,
                           bind=_engine)
    return session()


def recreate_session():
    global _session, _engine
    try:
        _session.close()
    except:
        print('failed to close session')
    _session = None
    _session = scoped_session(sessionmaker(autocommit=False,
                                           autoflush=True,
                                           expire_on_commit=False,
                                           bind=_engine))


def session():
    global _session
    return _session


def engine():
    global _engine
    return _engine


def dispose():
    global _engine, _session, metadata
    _session.close()
    _engine.dispose()
    _engine = None
    _session = None
    metadata.drop_all(bind=_engine)
    metadata = MetaData()


def init(uri):
    global _engine, _session, metadata
    if _engine == None and _session == None:
        _engine = create_engine(uri, encoding='utf-8', pool_recycle=3600)
        _session = scoped_session(sessionmaker(autocommit=False,
                                               autoflush=True,
                                               expire_on_commit=False,
                                               bind=_engine))
        metadata.create_all(bind=_engine)
