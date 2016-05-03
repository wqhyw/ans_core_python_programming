#! /usr/bin/env python

def CtoF(C):
    return C * 9 / float(5) + 32


def FtoC(F):
    return (F - 32) * (5 / float(9))

def test():
    print CtoF(20)
    print FtoC(90)

if __name__ == '__main__':
    test()