#! /usr/bin/env python

def mypop(alist):
    """
    @program: my version of list.pop()
    @param: alist => a list
    @return: elem of alist[-1]
    """

    tmp = alist[-1]
    alist.remove(tmp)
    return tmp


def test():
    a = [1,2,3,4,5]
    b = ['22', 21, [23123]]

    print "Before mypop(): ", a, b
    print "After mypop(): ",mypop(a), a, mypop(b), b


if __name__ == '__main__':
    test()
