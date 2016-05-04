#! /usr/bin/env python

def mystrip(str_s):
    slist = list(str_s)
    slist_r = slist[::-1]
    newslist = []
    start = 0
    end = 0

    for x in slist:
        if x != ' ':
            start = slist.index(x)
            break

    for y in slist_r:
        if y != ' ':
            end = len(slist) - slist_r.index(y)
            break

    return str_s[start:end]


def test():
    print "\"", mystrip("   |dweq weq qqwe q|   "), "\""

if __name__ == '__main__':
    test()
