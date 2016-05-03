#! /usr/bin/env python

def getsum(src):
    sum = 0
    for num in src:
        sum += num
    return sum

def getavg(src):
    sum = getsum(src)
    avg = float(sum) / len(src)
    return avg

def printmenu():
    print "MENU: "
    print "1. input"
    print "2. getsum"
    print "3. getavg"
    print "x. exit"

def test():
    src = []
    while True:
        printmenu()
        ch = raw_input('Your choice: ')
        if ch == '1':
            src = [eval(x) for x in raw_input("Input 5 nums: ").split()]
        elif ch == '2':
            print "sum = ", getavg(src)
        elif ch == '3':
            print "average", getavg(src)
        elif ch == 'x':
            break
        else:
            print "input error, please try again."

if __name__ == '__main__':
    test()
