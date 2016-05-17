#! /usr/bin/env python

def getfactors(num):
    """
    @program: get all factors of num
    @param: num
    @tparam: int
    @return: facts
    @rtype: list
    """

    facts = []
    if type(num) == type(1) and num > 1:
        for x in range(1, num + 1):
            if num % x == 0: facts.append(x)

    return facts


def test():
    print getfactors(-1)
    print getfactors(0)
    print getfactors(1)
    print getfactors(2)
    print getfactors(3)
    print getfactors(4)
    print getfactors(23)
    print getfactors(24)
    print getfactors('ad')
    print getfactors(3.2)
    print getfactors(20)


if __name__ == '__main__':
    test()
