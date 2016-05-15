#! /usr/bin/env python

num1 = int(raw_input("Input first num: "))
num2 = int(raw_input("Input second num: "))
num3 = int(raw_input("Input third num: "))
stype = int(raw_input("Input 0 for asc and 1 for desc: "))

print "Before sort:", num1, num2, num3

# 0 => acs, 1 => desc
if num1 > num2:
    num1 ,num2 = num2, num1

if num1 > num3:
    num1 ,num3 = num3, num1

if num2 > num3:
    num2, num3 = num3, num2

if stype == 1:
    num1, num3 = num3, num1

print "After sort:n" ,num1, num2, num3
