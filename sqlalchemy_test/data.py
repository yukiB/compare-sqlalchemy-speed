# -*- coding: utf-8 -*-

from __future__ import absolute_import, with_statement, print_function, unicode_literals
from joblib import Parallel, delayed
import random

names = ['John', 'Kevin', 'Shun']

def create_data(index, team_name):
    name = names[random.randint(0,len(names)-1)] + str(index)
    age = random.randint(10, 99)
    return (name, age, team_name)

def create_data_list(n_user=30000, n_team=10):
    teams = [chr(i) for i in range(65, 65+n_team)]
    data = Parallel(n_jobs=-1)([delayed(create_data)
                                (i, teams[i % n_team]) for i in range(n_user)])
    return data, teams
