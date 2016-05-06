#! /usr/bin/env python

def payment(balance, monthly):

    result = []
    while balance > 0:
        result.append(balance)
        balance -= monthly

    if result[-1] > 0:
        result.append(0.0)
    return result


def prtpm(pmlist):
    """
    @func: print payment
    @param: pmlist >=> payments
    @tparam: list
    """

    print "Amout remaining"
    print "Pymt#\tPaid\tBalance"
    print "-----\t------\t-------\t"
    for index, bl in enumerate(pmlist):
        delt = 0.0
        if index > 0:
            delt = pmlist[index - 1] - pmlist[index]
        print " %2d \t$%.2f\t$%.2f" % (index,  delt, bl)


def test():
    prtpm(payment(100, 16.13))


if __name__ == '__main__':
    test()
