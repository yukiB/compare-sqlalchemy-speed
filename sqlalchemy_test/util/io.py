# -*- coding: utf-8 -*-

from __future__ import absolute_import, with_statement, print_function, unicode_literals
import json
import os
import traceback
import csv
import codecs


def create_dir(dirpath, print_log=True):
    try:
        if not os.path.exists(dirpath):
            os.mkdir(dirpath)
        return True
    except:
        if print_log:
            traceback.print_exc()
            print("Failed create" + dirpath)
        return False


def remove_file(filepath, print_log=True):
    try:
        os.remove(filepath)
        return True
    except:
        if print_log:
            traceback.print_exc()
            print("Failed to remove " + filepath)
        return False


def load_json(filepath, encode=None, print_log=True):
    try:
        with codecs.open(filepath, 'r', encode) if encode else open(filepath, 'r') as f:
            data = json.load(f)
        return data
    except:
        if print_log:
            traceback.print_exc()
            print("Failed to load " + filepath)


def save_json(filepath, data, encode=None, print_log=True):
    # try:
    with codecs.open(filepath, 'w', encode) if encode else open(filepath, 'w') as f:
        json.dump(data, f)
    return True
    # xcept:
    if print_log:
        traceback.print_exc()
        print("Failed to save " + filepath)
    return False
