#! /usr/bin/env/ python

# -*- coding: utf-8 -*-

"""
Created on Fri Mar 11 19:31:58 2016

@program: RnMTextFile.py -- create, read and display text file

@author: LeO_wqHyw
"""

import os


def get_fname():
    """
    @program: get filename
    @return: filename
    @rtype: string
    """

    while True:
        fname = raw_input('input filename: ')
        if os.path.exists(fname):
            print "ERROR: '%s' already exists" % fname
        else:
            break
    return fname


def get_content():
    """
    @program: get file content (text) lines
    @return: all => all contents
    @rtype: list
    """

    all = []
    print "\nEnter lines ('.' by itself to quit).\n"
    while True:
        entry = raw_input('>> ')
        if entry == '.':
            break
        else:
            all.append(entry)
    return all


def create_file(fname):
    """
    @program: write lines to file with proper line-endings
    @param: fname => filename
    @ptype: string
    """

    ls = os.linesep
    all = get_content()
    fobj = open(fname, 'w')
    fobj.writelines(['%s%s' % (x, ls) for x in all])
    fobj.close()


def input_fname():
    """
    @program: input filename
    @rtype: string
    """

    return raw_input('Enter filename: ')


def display(fname):
    """
    @program: attempt to open file for reading and displaying
    @param: fname => filename
    @rparam: string
    @return: true or false
    @rtype: bool
    """

    try:
        fobj = open(fname, 'r')
    except IOError, e:
        print "*** file open error:", e
        return False
    else:
        for eachLine in fobj:
            print eachLine.strip()
        fobj.close()
        return True


def main():
    """
    @program: main function
    """

    choice = ''
    while True:
        if choice == 'w':
            create_file(get_fname())
            print 'Create done.'
            break
        elif choice == 'r':
            display(input_fname())
            break
        else:
            choice = raw_input("Enter w to write and r to read: ")


if __name__ == '__main__':
    main()
