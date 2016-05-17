#! /usr/bin/env python

def fib(n):
    """
    @program: get the nth of Fibonacci sequence
    @param: n => a integer bigger than 1
    @return: res
    @rtype: integer
    """
    res = 1
    if n > 2:
        f1 = 1
        f2 = 2
        for x in range(3, n+1):
            f1, f2 = f2, f2 + f1
        res = f1
    return res


def test():
    print fib(1)
    print fib(2)
    print fib(3)
    print fib(4)
    print fib(5)
    print fib(6)
    print fib(7)


if __name__ == '__main__':
    test()
