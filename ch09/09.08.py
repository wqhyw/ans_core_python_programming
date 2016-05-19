#! /usr/bin/env python

def main():
    modname = raw_input("Enter module name: ")
    try:
        mod = __import__(modname)
        names = dir(mod)
        for x in names:
            func = getattr(mod, x)
            print "name:", x
            print "type:", type(func)
            print "value:", func
    except ImportError:
        print 'No module named', modname


if __name__ == '__main__':
    main()
