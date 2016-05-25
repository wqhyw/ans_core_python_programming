#! /usr/bin/env python

def countlines(filename):
    """
    @program: count numbers of lines in filename
    @param: filename
    @return: cnt
    @rtype: int
    """
    cnt = 0
    try:
        f = open(filename, 'r')
        for line in f:
            cnt+=1
        f.close()
    except IOError:
        cnt = -1
    finally:
        return cnt


def main():
    print countlines('09.10.01')
    print countlines('09.10.02.py')


if __name__ == '__main__':
    main()
