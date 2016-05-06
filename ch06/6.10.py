#! /usr/bin/env python

import string


def transi(strin):
    """
    @func: make small letters in strin upper, big lower
    @return: string transived
    @rtype: string
    """

    def cmp(letter):
        # big letter lower, small letter upper

        if letter in string.letters[:25]:
            return string.upper(letter)
        else:
            return string.lower(letter)

    return ''.join(map(cmp, strin))


def test():
    print transi(raw_input("Input a string: "))


if __name__ == '__main__':
    test()
