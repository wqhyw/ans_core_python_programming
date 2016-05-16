#! /usr/bin/env python

def cal(A, B, op):
    """
    @program: cal A op B
    @param: A, B=> two set
            op => one operation in
                   {'in', 'not in', '&', '|', '^', '<', '<=', '>', '>=', '==', '!='}
    @return: res => result of A op B
    @rtype: set
    """

    ops = {'in', 'not in', '&', '|', '^', '<', '<=', '>', '>=', '==', '!='}
    res = set()
    if op in ops:
        if op == 'in': res = (A in B)
        elif op == 'not in': res = (A not in B)
        elif op == '&': res = (A & B)
        elif op == '|': res = (A | B)
        elif op == '^': res = (A ^ B)
        elif op == '<': res = (A < B)
        elif op == '<=': res = (A <= B)
        elif op == '>': res = (A > B)
        elif op == '>=': res = (A >= B)
        elif op == '==': res = (A == B)
        else: res = (A != B)
    else:
        print op, 'Not Support!'
    return res


def getset(setname):
    """
    @program: get a set from raw_input()
    @param: setname => name of set
    @rtype: set
    """
    promote = "Input set {name}, elements split by ',': ".format(name=setname)
    return set(raw_input(promote).split(','))


def main():
    A = getset('A')
    B = getset('B')
    op = raw_input("Input a op of set: ")

    print 'A =', A
    print 'B =', B
    print "A {op} B = {res}".format(op=op, res=cal(A, B, op))

if __name__ == '__main__':
    main()
