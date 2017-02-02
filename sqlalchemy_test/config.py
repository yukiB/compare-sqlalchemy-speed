# -*- coding: utf-8 -*-

from __future__ import absolute_import, with_statement, print_function, unicode_literals
import json
import sys

_config = {}


def load_config(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        print("Failed to load " + filepath)
        print("Unexpected error:" + str(sys.exc_info()[0]))


def set_db(filepath):
    global _config
    db_config = load_config(filepath)
    _config['DATABASE_URI'] = 'mysql://%s:%s@%s/%s?charset=utf8' % (
        db_config["user"], db_config["password"], db_config["host"], db_config["name"])


def set(filepath):
    global _config
    config = load_config(filepath)
    _config.update(config)


def keys():
    global _config
    return _config.keys()


def get(key):
    global _config
    try:
        return _config[key]
    except:
        print("Failed to get config %s" % key)
