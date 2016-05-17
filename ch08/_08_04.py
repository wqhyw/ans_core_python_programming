#! /usr/bin/env python

def isprime(num):
    """
    @program: check num is prime or not
    @param: num
    @tparam: int
    @return: True or False
    """

    if type(num) == type(1):
        if num == 0 or num == 1 or num < 0: return False
        if num == 2: return True
        for x in range(2, int(num**0.5)+1):
            if num % x == 0:
                return False
        else:
            return True
    else:
        return False


def test():
    print isprime(-1)
    print isprime(0)
    print isprime(1)
    print isprime(2)
    print isprime(3)
    print isprime(4)
    print isprime(23)
    print isprime(24)
    print isprime('ad')
    print isprime(3.2)


if __name__ == '__main__':
    test()
