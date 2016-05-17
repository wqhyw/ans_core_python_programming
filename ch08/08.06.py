#! /usr/bin/env python

from _08_04 import isprime
from _08_05 import getfactors

def fact(num):
    """
    @program: get fact of num
    @param: num
    @tparam: int
    @return: facts
    @rtype: list
    """

    allfacts = getfactors(num)
    facts = []
    if allfacts != []:
        primefacts = []
        for x in allfacts:
            if isprime(x): primefacts.append(x)
        for x in primefacts:
            done = False
            while not done:
                tmp = num % x
                if tmp == 0:
                    facts.append(x)
                    num //= x
                else: done = True
    return facts


def test():
    print fact(1)
    print fact(-1)
    print fact(0)
    print fact(2)
    print fact(3)
    print fact(4)
    print fact(25)
    print fact(26)
    print fact(3.2)
    print fact('ada')


if __name__ == '__main__':
    test()
