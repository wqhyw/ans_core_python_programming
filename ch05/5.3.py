#! /usr/bin/env python

def getevaluate(grade):
    if grade < 0 or grade > 100:
        return 'ERROR'
    elif grade <= 100 and grade >= 90:
        return 'A'
    elif grade >=80:
        return 'B'
    elif grade >=70:
        return 'C'
    elif grade >=60:
        return 'E'
    else:
        return 'F'

def test():
    print getevaluate(75)

test()