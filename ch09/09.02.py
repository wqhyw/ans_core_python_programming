#! /usr/bin/env python

def printNofF(N, F):
    """
    @program: print first N lines of of F
    @param: N, F
    """

    f = open(F, 'r')
    for x in range(N):
        print x+1,':', f.readline(),
    f.close()
    print 'Done!'


def main():
    while True:
        try:
            N = int(raw_input("Enter N: "))
            F = raw_input("Enter F: ")
            printNofF(N, F)
            break
        except (ValueError,TypeError):
            print "Invalid N! Please reenter."
        except IOError:
            print 'Invalid F! Please reenter.'


if __name__ == '__main__':
    main()
