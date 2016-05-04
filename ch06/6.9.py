#! /usr/bin/env python

def getinp():
    'Get a valid integer'

    while True:
        inp = raw_input("Input minutes: ")
        if inp.isdigit():
            return int(inp)
        else:
            print "Only integer is valid. Please try again."


def gethnm(minutes):
    'Get hours and minutes'

    return repr(minutes // 60) + ' h ' + repr(minutes % 60) + ' m'


def test():
    print gethnm(getinp())


if __name__ == '__main__':
    test()
