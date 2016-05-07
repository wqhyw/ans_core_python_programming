#! /usr/bin/env python

def getAns(money):

    if money > 1 or money < 0:
        print "Invalid money."
    else:
        money = int(money * 100)
        cent25 = divmod(money, 25)
        cent10 = divmod(cent25[1], 10)
        cent5 = divmod(cent10[1], 5)
        cent1 = cent5[1]
    return cent25[0], cent10[0], cent5[0], cent1


def test():
    ans = getAns(0.99)
    print "25 cent: ", ans[0]
    print "10 cent: ", ans[1]
    print "5 cent: ", ans[2]
    print "1 cent: ", ans[3]

if __name__ == '__main__':
    test()