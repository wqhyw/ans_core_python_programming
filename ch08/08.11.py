#! /usr/bin/env python

import re

def fix(errorname):
    """
    @program: fix invalid name to be like 'Lastname, Firstname'
    @param: errorname
    @return: validname
    @rtype: string
    """

    validname = ''
    namelist = []
    if re.match(r'[A-Z][a-z]+,[A-Z][a-z]+', errorname) is not None:
        namelist = errorname.split(',')
        validname = namelist[0] + ', ' + namelist[1]
    elif re.match(r'[A-Z][a-z]+ [A-Z][a-z]+', errorname) is not None:
        namelist = errorname.split()
        validname = namelist[0] + ', ' + namelist[1]
    elif re.match(r'([A-Z][a-z]+){2}', errorname) is not None:
        index = 0
        for x in range(1, len(errorname)):
            if errorname[x].isupper():
                index = x
        namelist.append(errorname[:index])
        namelist.append(errorname[index:])
        validname = namelist[0] + ', ' + namelist[1]
    else:
        pass

    return validname

def namecheck(name):
    """
    @program: check if name like 'Lastname, Firstname'
    @param: name
    @return: True or False
    """

    return False if re.match(r'[A-Z][a-z]+, [A-Z][a-z]+', name) is None else True


def main():
    """
    @program: get name and print
    """

    N = 0
    done = False
    names = []
    fixcnt = 0
    while not done:
        try:
            N = int(raw_input("Enter total number of names:"))
            done = True
        except (ValueError, TypeError):
            print ">>ERROR: Invalid input. Try again"

    for x in range(N):
        done = False
        tmp = ''
        promote = "Please enter name {nm}: ".format(nm=x)
        while not done:
            tmp = raw_input(promote)
            if not namecheck(tmp):
                fixcnt += 1
                print ">> Wrong format... should be Last, First.\n" \
                      ">> You have done this {ft} time(s) already." \
                      " Try to fix input...".format(ft=fixcnt)
                tmp = fix(tmp)
                if tmp == '':
                    print ">> Fix failed. Please reenter."
                else:
                    print ">> Fix done."
                    done = True
            else:
                done = True
        names.append(tmp)
    names.sort()
    print "The sorted list (by last name) is:\n", '\n'.join(names)


if __name__ == '__main__':
    main()

# Hamilton, Gerald
# Royce, Linda
# Salem, Winston
# Smith, Joe
# Wong, Mary