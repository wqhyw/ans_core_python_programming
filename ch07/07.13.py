#! /usr/bin/env python

def getset():
    """
    @program: generate a set of random numbers between 0 to 9, length between 1 to 10
    @return: res
    @rtype: set
    """

    import random
    res = set()
    length = random.randint(1,10)
    for x in xrange(length): res.add(random.randint(0, 9))
    return res


def main():
    A = getset()
    B = getset()

    print "A = {", ','.join(map(str, list(A))), "}"
    print "B = {", ','.join(map(str, list(B))), "}"
    print "A|B = {", ','.join(map(str, list(A|B))), "}"
    print "A&B = {", ','.join(map(str, list(A&B))), "}"


if __name__ == '__main__':
    main()
