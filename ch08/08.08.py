#! /usr/bin/env python

def factorial(num):
    """
   @program: get factorial of num
   @param: num
   @tparam: int
   @return: res
   @rtype: int
   """

    res = 1
    if type(num)== type(1) and num >= 0:
        if num != 0 and num != 1:
            for x in range(2, num+1):
                res *= x
    else:
        res = 0

    return res


def test():
    print factorial(-1)
    print factorial(0)
    print factorial(1)
    print factorial(2)
    print factorial(5)
    print factorial(8)
    print factorial(10)
    print factorial(3.2)
    print factorial('aa')


if __name__ == '__main__':
    test()
