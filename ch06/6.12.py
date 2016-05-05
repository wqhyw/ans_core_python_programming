#! /usr/bin/env python

# a) def findchr(string, char)
def findchr(string, char):
    'find char\'s index of string'

    if char in string:
        indexs = []
        for x in xrange(len(string)):
            if string[x] == char:
                indexs.append(x)
        return indexs
    else:
        return -1


# b) def rfindchr(string, char)
def rfindchr(string, char):
    'find last appearence of char'

    if char in string:

        for x in xrange(-1, -(len(string) + 1), -1):
            if string[x] == char:
                return  len(string) + x
    else:
        return -1


# c) def subchar(string, origchar, newchar)
def subchar(string, origchar, newchar):
    'find origcahr the replace it'

    indexs = findchr(string, origchar)

    if  indexs != -1:
        string_list = list(string)
        for x in indexs:
            string_list[x] = newchar
        else:
            return ''.join(string_list)
    else:
        return string


def test():
    print 'dasdae fx'
    print findchr('dasdae fx', 'a')
    print rfindchr('dasdae fx', 'a')
    print subchar('dasdae fx', 'Z', 'A')


if __name__ == '__main__':
    test()
