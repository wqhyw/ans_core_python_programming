#! /usr/bin/env python

db1 = {1:'a', 2:'b', 3:'c'}
db2 = {}

for k,v in db1.items():
    db2[v] = k

print db1
print db2