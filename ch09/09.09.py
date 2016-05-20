#! /usr/bin/env python

from os import walk as ls
from os.path import join as jn


def getstd():
    """
    @program: get all files and their path in python standard libs
    @return: pys => key = module name, value = full path
    @rtype: dict
    """
    root = r'C:\MyApps\py2.7\Lib'
    full = ls(root)
    pys = {}
    for parent, dirs, files in full:
        for fi in files:
            if '__init__' not in fi and fi[-1] == 'y':
                pys[fi[:-3]] = jn(parent, fi)
    return pys


# TODO
