#! /usr/bin/env python

# import module
import string

# infinity loop to get a correct input
while 1:

    # get input
    num_str = raw_input('Enter a number: ')

    # check input
    try:
        # string to number
        num_num = string.atoi(num_str)

        # quit loop
        break

    # handle invalid input
    except ValueError:
        print "invalid input... try again"

# get all integers between 1 to num(including)
fac_list = range(1, num_num+1)
print "BEFORE:", `fac_list`


# my version

cp_fac = []

for x in fac_list:
    if num_num % x == 0:
        cp_fac.append(x)
else:
    fac_list = cp_fac


'''
# set start
i = 0

# start loop end with list traveled
while i < len(fac_list):

    # find fac
    if num_num % fac_list[i] != 0:
        del fac_list[i]

    # counter increase
    i = i+1
'''

#print result
print "AFTER:", `fac_list`
