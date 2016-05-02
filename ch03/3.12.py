#! /usr/bin/env/ python

# -*- coding: utf-8 -*-

"""
Created on Fri Mar 11 19:31:58 2016

@program: RnMTextFile.py -- create, read and displaytext file

@author: LeO_wqHyw
"""

# create part
import os

def get_fname():
    'get_fname(): get filename'

    while True:
        fname = raw_input('input filename: ')
        if os.path.exists(fname):
            print "ERROR: '%s' already exists" % fname
        else:
            break
    return fname

def get_content():
    'get_content(): get file content (text) lines'

    all = []
    print "\nEnter lines ('.' by itself to quit).\n"
    #loop until user terminates input
    while True:
        entry = raw_input('>> ')
        if entry == '.':
            break
        else:
            all.append(entry)
    return all

def create_file(fname):
    'create_file(fname): write lines to file with proper line-endings'

    ls = os.linesep
    all = get_content()
    fobj = open(fname, 'w')
    fobj.writelines(['%s%s' % (x, ls) for x in all])
    fobj.close()
    return True

# read and display part
def input_fname():
    'input_fname(): input filename'

    return raw_input('Enter filename: ')

def display(fname):
    'display(fname): attempt to open file for reading and displaying'

    try:
        fobj = open(fname, 'r')
    except IOError, e:
        print "*** file open error:", e
        return False
    else:
        # display contents to the screen
        for eachLine in fobj:
            print eachLine.strip()
        fobj.close()
        return True

def main():
    'main function'

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
    return True


if __name__ == '__main__':
    main()
