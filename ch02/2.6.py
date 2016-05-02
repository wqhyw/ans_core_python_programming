#! /usr/bin/env python

# a) Codes Below:
num = 1
if num > 0:
    print num, "is positive number."
elif num == 0:
    print num, "is zero."
elif num < 0:
    print num, "is negative number."
else:
    print "Input error."


# b) Codes Below:
num = int(raw_input("Input a integer: "))

if num > 0:
    print num, "is positive number."
elif num == 0:
    print num, "is zero."
elif num < 0:
    print num, "is negative number."
else:
    print "Input error."