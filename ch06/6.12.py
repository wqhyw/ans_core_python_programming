#! /usr/bin/env python

# a) def findchr(string, char)
def findchr(src, char):
    """
    @program: find char's index of string
    @param: src => source string
            char => letter need to find index
    @tparam: string
    @return: indexs =>a list of index of char when found
             -1 => char not found
    @rtype: list or int
    """

    if char in src:
        indexs = []
        for x in xrange(len(src)):
            if src[x] == char:
                indexs.append(x)
        return indexs
    else:
        return -1


# b) def rfindchr(string, char)
def rfindchr(src, char):
    """
    @program: find last appearence of char
    @param: src => source string
            char => letter need to find index
    @tparam: string
    @return: index when char found
             -1 => char not found
    @rtype: int
    """

    if char in src:

        for x in xrange(-1, -(len(src) + 1), -1):
            if src[x] == char:
                return  len(src) + x
    else:
        return -1


# c) def subchar(string, origchar, newchar)
def subchar(src, origchar, newchar):
    """
    @program: find origcahr then replace it by newchar
    @param: src => source string
            origchar => letter need to be found
            newchar => relacement when origcahr found
    @tparam: string
    @return: src relaced when origchar found
             src not relaced when origchar not found
    @rtype: string
    """

    indexs = findchr(src, origchar)

    if  indexs != -1:
        string_list = list(src)
        for x in indexs:
            string_list[x] = newchar
        else:
            return ''.join(string_list)
    else:
        return src


def test():
    print 'dasdae fx'
    print findchr('dasdae fx', 'a')
    print rfindchr('dasdae fx', 'a')
    print subchar('dasdae fx', 'Z', 'A')


if __name__ == '__main__':
    test()
