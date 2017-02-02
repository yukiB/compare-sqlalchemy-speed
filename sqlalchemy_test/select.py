# -*- coding: utf-8 -*-

from __future__ import absolute_import, with_statement, print_function, unicode_literals
from sqlalchemy import select, desc
import sqlalchemy_test.database as database
from sqlalchemy_test.model.user import User
from sqlalchemy_test.model.team import Team
from multiprocessing import Pool
import multiprocessing as multi


limit = 100


def select_teams_orm():
    return Team.query().all()


def select_teams_core():
    t = Team.__table__.c
    sel = select([t.id, t.name]).select_from(Team.__table__)
    res = database.session().execute(sel)
    result = [{'id': r[0], 'name': r[1]} for r in res]
    return result


def select_user_team_orm():
    teams = select_teams_orm()
    users = [User.query()\
                      .filter(User.team == tm)\
                      .order_by(desc(User.age)).limit(limit).all() for tm in teams]
    result = [{'id':team.id,
               'name':team.name,
               'users': [{'id': u.id, 'name': u.name, 'age': u.age}
                         for u in user]}
              for team, user in zip(teams, users)]
    return result


def select_user_team_core():
    u = User.__table__.c
    teams = select_teams_core()
    query = lambda team_id:\
            select([u.id, u.name, u.age]).select_from(User.__table__)\
                                         .where(u.team_id == team_id)\
                                         .order_by(desc(u.age)).limit(limit)
    res_list = [database.session().execute(query(tm['id'])) for tm in teams]
    result = [{'id': t['id'],
               'name': t['name'],
               'users': [{'id': r[0], 'name': r[1], 'age': r[2]}
                         for r in res]}
              for t,res in zip(teams, res_list)]
    return result


_session = None

def select_user_team(team):
    global _session
    u = User.__table__.c
    session = _session if _session else database.session()
    sel = select([u.id, u.name, u.age]).select_from(User.__table__)\
                                       .where(u.team_id == team['id'])\
                                       .order_by(desc(u.age)).limit(limit)
    users = [{'id': r[0], 'name': r[1], 'age': r[2]}
             for r in session.execute(sel)]
    return {'id': team['id'],
            'name': team['name'],
            'users': users}


def select_user_team_multi(single=False):
    global _session
    teams = select_teams_core()
    _session = database.create_local_session()
    if not single:
        try:
            p = Pool(multi.cpu_count())
        except:
            single = True
    try:
        if not single:
            result = p.map(select_user_team, teams)
            p.close()
        else:
            result = [select_user_team(t) for t in teams]
        _session.close()
    except:
        _session.close()
        if not single:
           return select_user_team_multi(True)
        else:
            database.recreate_session()
            result = []
            
    return result
    

def select_data_team(option):
    if option == 'orm':
        result = select_user_team_orm()
    elif option == 'core':
        result = select_user_team_core()
    elif option == 'multi':
        result = select_user_team_multi()
    else:
        print('option is wrong')
        result = []
    return result


def select_user_orm():
    users = User.query().order_by(desc(User.age)).limit(limit).all()
    result = [{'id': u.id, 'name': u.name, 'age': u.age, 'team': u.team.name}
              for u in users]
    return result


def select_user_core():
    u = User.__table__.c
    t = Team.__table__.c
    sel = select([u.id, u.name, u.age, t.name])\
          .select_from(User.__table__.join(Team.__table__, t.id == u.team_id))\
          .order_by(desc(u.age)).limit(limit)
    result = [{'id': r[0], 'name': r[1], 'age': r[2], 'team': r[3]}
              for r in database.session().execute(sel)]
    return result


def get_user(r):
    return {'id': r[0], 'name': r[1], 'age': r[2], 'team': r[3]}


def select_user_multi():
    u = User.__table__.c
    t = Team.__table__.c
    sel = select([u.id, u.name, u.age, t.name])\
          .select_from(User.__table__.join(Team.__table__, t.id == u.team_id))\
          .order_by(desc(u.age)).limit(limit)
    p = Pool(multi.cpu_count())
    result = p.map(get_user, database.session().execute(sel))
    p.close()
    return result


def select_data_user(option):
    if option == 'orm':
        result = select_user_orm()
    elif option == 'core':
        result = select_user_core()
    elif option == 'multi':
        result = select_user_multi()
    else:
        print('option is wrong')
        result = []
    return result


def select_data(option, select_type):
    if select_type == 'team':
        result = select_data_team(option)
    elif select_type == 'user':
        result = select_data_user(option)
    else:
        print('select_type is wrong')
        result = []
    return result
