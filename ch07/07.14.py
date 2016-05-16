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

    index = 0
    while index < 3:
        inp = map(int, raw_input("Enter your A|B: ").split())
        if inp != list(A|B):
            print 'A|B incorrect. Try again.'
            index += 1
        else:
            print "Correct!"
            break
    else:
        print "A|B = {", ','.join(map(str, list(A|B))), "}"

    index = 0
    while index < 3:
        inp = map(int, raw_input("Enter your A&B: ").split())
        if inp != list(A&B):
            print 'A&B incorrect. Try again.'
            index += 1
        else:
            print "Correct!"
            break
    else:
        print "A&B = {", ','.join(map(str, list(A&B))), "}"


if __name__ == '__main__':
    main()
