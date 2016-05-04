#! /usr/bin/env python

strs = list(raw_input("Input a string: "))
strs_r = strs[::-1]

# a) codes below
print "forward:", ' '.join(strs)
print "backward", ' '.join(strs_r)

# b) dis=true => A != a, dis=false => A == a
def strcmp(str, dis = True):
    # TODO
    pass
