#! /usr/bin/env python

from string import letters as ls

def parseini(ininame):
    """
    @program: parse a *.ini file
    @param: ininame => name of the ini file, path including
    @return: res
    @rtype: dict
    """

    res = dict()
    try:
        inifile = open(ininame, 'r')
        tmpkeyofres = ''
        valid = ls + '#[\n'
        for line in inifile:
            if line[0] in valid:
                if line[0] == '#' or line[0] == '\n':
                    continue
                elif line[0] == '[':
                    tmpkeyofres = line[1:-2]
                    res[tmpkeyofres] = {}
                else:
                    value = line.split('=')
                    if value[1][-1] == '\n': value[1] = value[1][:-1]
                    res[tmpkeyofres][value[0]] = value[1]
        else:
            inifile.close()
    except IOError:
        print 'File open failed.'
    finally:
        return res


def test():
    print parseini('noname.ini')


if __name__ == '__main__':
    test()
