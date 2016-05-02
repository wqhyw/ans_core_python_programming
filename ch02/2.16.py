#! /usr/bin/env python

filename = raw_input("Input file name: ")
fobj = open(filename, 'r')
for line in fobj:
    print line,
fobj.close()