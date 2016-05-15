#! /usr/bin/env python

def display(seq, cloumns = 3, dest = 'n', rev = False):
    """
    @program: Given any number of items in a sequence or
              other container, display them in equally-
              distributed number of columns.
    @param: seq => a iterator type
            cloumns => vertial amounts
            dest => 'h' for horizontel, 'v' for vertical, 'n' for don't sort
            rev => True for DESC, False for ASC
    """

    if cloumns < 1:
        print "Cloumns too small."
    else:
        if dest == 'h':
            tmp = []
            for x in xrange(len(seq) + 1):
                if x < len(seq):

                    tmp.append(seq[x])
                    if len(tmp) == cloumns:
                        print '\t'.join(map(str, sorted(tmp, reverse=rev)))
                        tmp =[]

                else:
                    print '\t'.join(map(str, sorted(tmp, reverse=rev)))

        elif dest == 'v':
            tmp = [seq[x::cloumns] for x in xrange(cloumns)]
            for x in xrange(len(tmp)):
                tmp[x].sort(reverse=rev)
            r = len(tmp[0])
            for x in xrange(r):
                for y in xrange(cloumns):
                    if x < len(tmp[y]):
                        print tmp[y][x], '\t',
                    else:
                        print ' ',
                print

        elif dest == 'n':
            for x in xrange(len(seq)):
                print seq[x], '\t',
                if (x + 1) % 3 == 0:
                    print
            print

        else:
            print "Invaild dest."


def test():
    display([4,5,6,3,1,2,7,9,2,5,3,89,5])
    print
    display([4,5,6,3,1,2,7,9,2,5,3,89,5], dest='h')
    print
    display([4,5,6,3,1,2,7,9,2,5,3,89,5], dest='v')


if __name__ == '__main__':
    test()
