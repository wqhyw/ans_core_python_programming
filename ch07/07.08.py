#! /usr/bin/env python

db = []
nums = 0

while True:
    try:
        N = int(raw_input('Input employee amounts: '))
    except ValueError:
        print 'Invalid input. Please try again'
    else:
        nums = N
        break

for x in xrange(1, nums+1):
    name = raw_input(r"#%d's name: " % x)
    num = raw_input(r"#%d's number: " % x)
    db.append([name, num])
    print
else:
    print "Done!\n"

db.sort(key=lambda x:x[0])
for x in db:
    print 'Name:%s, Num: %s'%(x[0], x[1])

print

db.sort(key=lambda x:x[1])
for x in db:
    print 'Name:%s, Num: %s'%(x[0], x[1])
