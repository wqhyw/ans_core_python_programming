#! /usr/bin/env python

import string


def transi(strin):
    def cmp(letter):
        if letter in string.letters[:25]:
            return string.upper(letter)
        else:
            return string.lower(letter)
    return ''.join(map(cmp, strin))


def test():
    print transi(raw_input("Input a string: "))


if __name__ == '__main__':
    test()
