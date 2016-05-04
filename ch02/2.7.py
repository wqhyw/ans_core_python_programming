#! /usr/bin/env python

strs = list(raw_input("Input a string: "))

# a) By for:
print ' '.join(strs)

print

# b) By while:
cnt = 0;

while cnt < len(strs):
    print strs[cnt],
    cnt += 1
