#! /usr/bin/env python

# src = [x for x in xrange(5)]
src = [eval(x) for x in raw_input("Input 5 nums: ").split()]
sum = 0

for num in src:
    sum += num

print sum


