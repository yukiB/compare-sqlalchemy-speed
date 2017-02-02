# -*- coding: utf-8 -*-

from __future__ import absolute_import, with_statement, print_function, unicode_literals
import sqlalchemy_test.database as database
from sqlalchemy_test.model.user import User
from sqlalchemy_test.model.user import UserTable
from sqlalchemy_test.model.team import Team
from joblib import Parallel, delayed
import time, sys


def insert_team(team_name):
    t = Team(team_name)
    database.session().add(t)
    database.session().commit()
    return Team.query().filter(Team.name == team_name).first()


def insert_user(name, age, team):
    u = User(name, age, team)
    database.session().add(u)
    database.session().commit()


def single_insertion(data_list, team_list):
    team_dict = {t: insert_team(t) for t in team_list}
    start = time.time()
    [insert_user(d[0], d[1], team_dict[d[2]]) for d in data_list]
    sys.stderr.write('SqlAlchemy ORM: ')
    print('elapsed time of insertion: {0:.3f} [sec]'.format(time.time() - start))


def multi_insertion(data_list, team_list):
    teams = [Team(t) for t in team_list]
    database.session().add_all(teams)
    database.session().commit()
    teams = Team.query().all()
    team_dict = {t.name: t for t in teams}
    # Parallelにorm objectは渡せない
    # users = Parallel(n_jobs=-1)([delayed(User)
    #                             (d[0], d[1], team_dict[d[2]]) for d in data_list])
    users = [User(d[0], d[1], team_dict[d[2]]) for d in data_list]
    start = time.time()
    database.session().add_all(users)
    database.session().commit()
    sys.stderr.write('SqlAlchemy ORM multi insert: ')
    print('elapsed time of insertion: {0:.3f} [sec]'.format(time.time() - start))
    
    
def bulk_insertion(data_list, team_list):
    teams = [Team(t) for t in team_list]
    database.session().add_all(teams)
    database.session().commit()
    teams = Team.query().all()
    team_dict = {t.name: t for t in teams}
    start = time.time()
    # database.session().bulk_save_objects(users, return_defaults=True)
    database.session().bulk_save_objects(
        [UserTable(name=d[0],
                   age=d[1],
                   team_id=team_dict[d[2]].id,
                   updated_at = time.time(),
                   created_at = time.time())
         for d in data_list], return_defaults=True)
    database.session().commit()
    sys.stderr.write('SqlAlchemy ORM bulk insert: ')
    print('elapsed time of insertion: {0:.3f} [sec]'.format(time.time() - start))


def core_insertion(data_list, team_list):
    teams = [Team.create_dict(t) for t in team_list]
    database.session().execute(Team.__table__.insert(), teams)
    database.session().commit()
    team_dict = {t: i + 1 for i, t in enumerate(team_list)}
    users = Parallel(n_jobs=-1)([delayed(User.create_dict)
                                 (d[0], d[1], team_dict[d[2]]) for d in data_list])
    #users = [User.create_dict(d[0], d[1], team_dict[d[2]]) for d in data_list]
    start = time.time()
    database.session().execute(User.__table__.insert(), users)
    database.session().commit()
    sys.stderr.write('SqlAlchemy core bulk insert: ')
    print('elapsed time of insertion: {0:.3f} [sec]'.format(time.time() - start))

    
def insert_data(data_list, team_list, option):
    if option == 'single':
        single_insertion(data_list, team_list)
    elif option == 'multi':
        multi_insertion(data_list, team_list)
    elif option == 'bulk':
        bulk_insertion(data_list, team_list)
    elif option == 'core':
        core_insertion(data_list, team_list)
    else:
        print('option is wrong')
