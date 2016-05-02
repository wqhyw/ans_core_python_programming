# ! /usr/bin/env python


def isnumber(num):
    'Check num is a integer or float'

    tmp = num.split('.')
    intcondition = (len(tmp) == 1) and tmp[0].isdigit()
    floatcondition = (len(tmp) == 2) and tmp[0].isdigit() and tmp[1].isdigit()

    if intcondition:
        return 1
    elif floatcondition:
        return 2
    else:
        return 0


def strtonum(str, strtype):
    'string to number'

    if strtype == 1:
        return int(str)
    elif strtype == 2:
        return float(str)
    else:
        return None


def getexpression():
    'Input a valid expreesion'

    while True:
        exp = raw_input("Input your expression: ").split()
        if len(exp) == 3:
            left = strtonum(exp[0], isnumber(exp[0]))
            right = strtonum(exp[2], isnumber(exp[2]))

            if left is None or right is None:
                print "Invalid expression"
            else:
                return left, exp[1], right
        else:
            print "Invalid expression"


def simplecal(expression):
    'Calculate the expression'

    ops = {'+', '-', '*', '/', '%', '**'}
    left = expression[0]
    right = expression[2]
    op = expression[1]

    if op in ops:
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            if left % right == 0:
                return left / right
            else:
                return left / float(right)
        elif op == '%':
            return left % right
        elif op == '**':
            return  left ** right
        else:
            print "Operator not support"
            return None


def test():
    print simplecal(getexpression())

if __name__ == '__main__':
    test()
