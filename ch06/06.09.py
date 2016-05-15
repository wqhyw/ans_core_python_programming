#! /usr/bin/env python

def getinp():
    """
    @func: Get a valid integer
    @return: the integer from raw_input()
    """

    while True:
        inp = raw_input("Input minutes: ")
        if inp.isdigit():
            return int(inp)
        else:
            print "Only integer is valid. Please try again."


def gethnm(minutes):
    """
    @func: Get hours and minutes
    @param: minutes
    @return: time like (x h x m)
    """

    return repr(minutes // 60) + ' h ' + repr(minutes % 60) + ' m'


def test():
    print gethnm(getinp())


if __name__ == '__main__':
    test()
