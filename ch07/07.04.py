#! /usr/bin/env python

k = [1,2,3,4,5]
v = ['a', 'b', 'c', 'd', 'e']
d = {x:y for x, y in zip(k,v)}

print d
