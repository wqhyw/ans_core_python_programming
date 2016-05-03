#! /usr/bin/env python

def snc(str1, str2):
    'number in string campare'

    if str1.isdigit() and str2.isdigit():
        nlist1, nlist2 = list(str1), list(str2)
        min = len(nlist1) if len(nlist1) < len(nlist2) else len(nlist2)

        for x in xrange(min):
            if nlist1[x] > nlist2[x]:
                return 1
            elif nlist1[x] < nlist2[x]:
                return -1
            else:
                pass
        else:
            return 0
    else:
        return None


def main():
    while True:
        inp = raw_input("Input a list of numbers: ").split()
        for x in inp:
            if x.isdigit() == 0:
                print "Only numbers is valid."
                break
        else:
            print "num sort:",
            print ' '.join(sorted([x for x in inp], key=eval, reverse=True))
            print "dict sort:",
            print ' '.join(sorted([x for x in inp], cmp=snc, reverse=True))
            break

if __name__ == '__main__':
    main()
