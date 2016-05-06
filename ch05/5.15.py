#! /usr/bin/env python

def GCD(m, n):
    """
    @func: get GCD of m, n
    @param: m, n => two integer
    @return: GCD of m and n
    """

    while True:
        r = m % n
        m, n = n, r
        if r == 0:
            return m


def LCM(m, n):
    """
        @func: get LCM of m, n
        @param: m, n => two integer
        @return: LCM of m and n
        """

    return m * n / GCD(m, n)


def test():
    print GCD(3, 2)
    print LCM(3, 2)


if __name__ == '__main__':
    test()
