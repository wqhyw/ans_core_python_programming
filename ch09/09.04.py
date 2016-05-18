#! /usr/bin/env python

def main():
    try:
        filename = raw_input("Enter filename(Path including): ")
        f = open(filename, 'r')
        cnt = 1
        page = 1
        for line in f:
            print cnt, ':', line,
            if cnt % 25 == 0:
                print 'Page', page
                raw_input("Enter any key to continue.\n")
                page += 1
            cnt += 1
        if (cnt-1) % 25 != 0:
            print 'Page', page
            print '\nDone!'
        else:
            print 'Done!'
    except IOError:
        print 'FILE OPEN ERROR.'
        print 'Failed!'


if __name__ == '__main__':
    main()
