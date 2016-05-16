#! /usr/bin/env python

def tr(srcstr, dststr, source):
    """
    @program: replace part of source to dststr
    @param: srcstr=>raw string
            dststr=>replace to
            source=>to be replaced
    @return: result=>source replaced
    @rtype: string
    """

    start = source.find(srcstr)
    if start != -1: end = start + len(srcstr)
    left = source[:start]
    right = source[end:]
    return left+dststr+right


def test():
    print tr('abce', 'mno', 'abcedef')


if __name__ == '__main__':
    test()
