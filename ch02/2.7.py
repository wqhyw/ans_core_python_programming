#! /usr/bin/env python

strs = raw_input("Input a string: ")

strs_len = len(strs)

# a) By for:
for index in xrange(strs_len):
    print strs[index],

print

# b) By while:
cnt = 0;

while cnt < strs_len:
    print strs[cnt],
    cnt += 1
