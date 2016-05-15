#!/usr/bin/env python

import string
import keyword

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v2.0'

inp = raw_input('Identifier to test: ')

if keyword.iskeyword(inp):
    print "Invalid: it is a python keyword"
else:
    if inp[0] not in alphas:
            print "Invalid: first symbol must be alphabetic or _"
    else:
        if len(inp) > 1:
            for otherChar in inp[1:]:
                if otherChar not in alphas + nums:
                    print "Invalid: remaining symbols must be alphanumeric"
                    break
                else:
                    print "Okay as an identifier"
        elif len(inp) == 1:
            if inp in string.letters:
                print "Okay as an identifier"
            elif inp == '_':
                print "Invalid: _ is not an identifier"
            elif inp in nums:
                print "Invalid: first symbol must be alphabetic or _"
