#! /usr/bin/env python

def strtofloat(str):
    """
    @progam: make a string to float
    @param: str
    @return: a flaot when succed or None when failed
    """
    for x in str.split('.'):
        if x.isdigit() == False:
            print "Invalid param"
            return 0
    else:
        return float(str)


def atoc(cpm):
    """
    @program: makea string to a complex object
    @param: cpm => a string like (1+2j)
    @return: result
    @rtype: complex object
    """

    cpm = [x for x in cpm.split("+")]
    print cpm
    if len(cpm) == 1:
        if cpm[0][-1] != 'j':
            return complex(strtofloat(cpm[0]), 0)
        else:
            return complex(0,strtofloat(cpm[0][:-1]))
    elif len(cpm) == 2:
        left = strtofloat(cpm[0])
        right = strtofloat(cpm[1][:-1])
        return complex(left, right)
    else:
        return None


def test():
    print atoc("2.2")

if __name__ == '__main__':
    test()
