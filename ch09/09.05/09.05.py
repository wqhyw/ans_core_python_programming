#! /usr/bin/env python

from functools import partial
import shelve

scoreopen = partial(shelve.open, 'score')


def savescores():
    """
    @program: input scores and save
    """

    try:
        N = int(raw_input('Enter amounts: '))
        fd = scoreopen('w')
        cnt = 0
        for x in range(1, N+1):
            done = False
            while not done:
                try:
                    name = raw_input("Enter name {cnt}: ".format(cnt=cnt+1))
                    sc = int(raw_input("Enter score {cnt}: ".format(cnt=cnt+1)))
                    if 0 <= sc <= 100:
                        if name in fd:
                            print "Record of {nm} exists. Score will upate.".format(nm=name)
                        fd[name] = sc
                        cnt += 1
                        done = True
                    else:
                        print "Score must between 0 and 100! Please reenter."
                except (ValueError, TypeError):
                    print "Invalid input! Please reenter."
        else:
            fd.close()
            print 'Done!'
    except (IOError, ValueError, TypeError):
        print "ERROR OCCURRED!"
        print "Save score Failed."


def getgrade():
    """
    @program: read scores from file and get grade
    @return: res
    @rtype: dict
    """

    grade = ['F', 'F', 'F', 'F', 'F', 'F', 'D', 'C', 'B', 'A', 'A']
    res = {}
    try:
        fd = scoreopen('r')
        for name in fd.keys():
            res[name] = grade[fd[name] // 10]
        fd.close()
    except IOError:
        print 'ERROR OCCURRED!'
        print 'Get grade Failed.'
    finally:
        return res


def clearscores():
    """
    @program: clear scores file
    """
    try:
        fd = scoreopen('n')
        fd.close()
    except IOError:
        print 'ERROR OCCURRED!'
        print 'Clear Failed.'


def printscores():
    """
    @program: print scores in file
    """
    try:
        fd = scoreopen('r')
        print fd
        fd.close()
    except IOError:
        print 'ERROR OCCURRED!'
        print 'Print scores Failed.'


def main():
    savescores()
    printscores()
    print getgrade()
    clearscores()
    printscores()

if __name__ == '__main__':
    main()
