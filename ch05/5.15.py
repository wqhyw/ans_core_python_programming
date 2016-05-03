#! /usr/bin/env python

def GCD(m, n):
    'get GCD of m, n'

    while True:
        r = m % n
        m, n = n, r
        if r == 0:
            return m


def LCM(m, n):
    return m * n / GCD(m, n)


def test():
    print GCD(3, 2)
    print LCM(3, 2)


if __name__ == '__main__':
    test()
