#! /usr/bin/env python

def isleap(year):
    condition0 = (type(year) == type(1))
    condition1 = (year % 4 == 0) and (year % 100 != 0)
    condition2 = (year % 400 == 0)

    if condition0:
        if condition1 or condition2:
            return True
        else:
            return False
    else:
        print year, "is invalid."
        return False

def test():
    print isleap(2015)

if __name__ == '__main__':
    test()