#! /usr/bin/env python

# a) even num between 0 - 20
for evens in xrange(0, 21, 2):
    print evens,

print

# b) odd num betweent 0 - 20
for odds in xrange(1, 20, 2):
    print odds,

print


# c)
def isdiv(num1, num2):
    return True if num1 % num2 == 0 else False


def test():
    num1 = int(raw_input("Input the first integer: "))
    num2 = int(raw_input("Input the second integer: "))
    print isdiv(num1, num2)

if __name__ == '__main__':
    test()

