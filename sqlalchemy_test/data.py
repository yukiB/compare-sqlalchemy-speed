# -*- coding: utf-8 -*-

from __future__ import absolute_import, with_statement, print_function, unicode_literals
# from joblib import Parallel, delayed
from multiprocessing import Pool
import multiprocessing as multi
import random

names = ['John', 'Kevin', 'Shun']

_teams = []
_n_team = 0

def create_data(index):
    global _teams, _n_team
    team_name = _teams[index % _n_team]
    name = names[random.randint(0,len(names)-1)] + str(index)
    age = random.randint(10, 99)
    return (name, age, team_name)


def create_data_list(n_user=30000, n_team=10):
    global _teams, _n_team
    _teams = [chr(i) for i in range(65, 65+n_team)]
    _n_team = n_team
    p = Pool(multi.cpu_count())
    data = p.map(create_data, range(n_user))
    p.close()
    #data = Parallel(n_jobs=-1)([delayed(create_data)
    #                            (i, teams[i % n_team]) for i in range(n_user)])
    return data, _teams
