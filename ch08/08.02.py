#! /usr/bin/env python

def getinp():
    """
    @program: get from to steps from user
    @return: F, T, S
    @rtype: integer
    """
    while True:
        try:
            F = int(raw_input("Input From: "))
            T = int(raw_input("Input To: "))
            S = int(raw_input("Input Steps: "))
            return ','.join(map(str, range(F, T+S, S)))
        except ValueError:
            print "Invalid input! Try again\n"


def test():
    print getinp()


if __name__ == '__main__':
    test()
