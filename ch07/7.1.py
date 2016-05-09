#! /usr/bin/env python

dict1 = {'1': 1}
dict2 = {'2': 2}

print dict(dict1.items()+dict2.items())
print dict(dict1, **dict2)