#! /usr/bin/env python

from _08_05 import getfactors

def isperfect(num):
    """
    @program: check if num is perfect number or not
    @param: num
    @tparam: int
    @return: True or False
    """

    factors = getfactors(num)
    if factors != []:
        parts = factors[:-1]
        sum = 0
        for x in parts: sum += x
        if sum == num: return True
    return False


def test():
    for x in xrange(10000):
        if isperfect(x): print x,


if __name__ == '__main__':
    test()
