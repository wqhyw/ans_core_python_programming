#! /usr/bin/env python

d = {'ab': 1, 'bc': 2, 'ccc': 3}
keys = sorted(d.keys())

for x in keys:
    print x,

print

for x in keys:
    print x, ':', d[x],

print

val = {v:k for k, v in d.items()}
vkeys = sorted(val.keys())
for x in vkeys:
    print val[x], ':', x,
