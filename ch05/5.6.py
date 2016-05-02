#! /usr/bin/env python

def isnumber(num):
    tmp = num.split('.')

    intcondition = (len(tmp) == 1) and tmp[0].isdigit()
    floatcondition = (len(tmp) == 2) and tmp[0].isdigit() and tmp[1].isdigit()

    if intcondition:
        return 1
    elif floatcondition:
        return 2
    else:
        return 0

def getexpression():
    while True:
        exp = raw_input("Input your expression: ").split()
        if len(exp) != 3:
            print "Invalid expression"
        else:
            left = exp[0]
            right = exp[2]
            lefttype = isnumber(left)
            righttype = isnumber(right)

            if isnumber(left) and isnumber(right):
            //TODO




def simplecal(expression):
    ops = {'+' : 1, '-' : 2, '*' : 3, '/' : 4, '%' : 5, '**' : 6}

    if ops.has_key(expression[1]):

    else:
        print "operator not support."




