#! /usr/bin/env python

while True:
    src = int(raw_input("Input a num between 1 and 100: "))
    if src < 101 and src > 0:
        print "Done."
        break
    else:
        print "Input error, please try again."
