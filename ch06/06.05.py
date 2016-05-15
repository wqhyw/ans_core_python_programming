#! /usr/bin/env python

strs = list(raw_input("Input a string: "))
strs_r = strs[::-1]

# a) codes below
print "forward:", ' '.join(strs)
print "backward", ' '.join(strs_r)

# b) dis=true => A != a, dis=false => A == a
def strcmp(str1, str2, dis = True):
    flag = False

    if len(str1) == len(str2):
        for left,right in zip(str1, str2):
            if (dis and (left != right)) or (dis == False and (left.lower() != right.lower())):
                break
        else:
            flag = True

    return flag


# c) palindromic check
def ispalindromic(str_s):
    str_r = ''.join(list(str_s)[::-1])
    return strcmp(str_s, str_r)


# d) make a string palindromic
def mkpalindromic(str_s):
    str_r = ''.join(list(str_s)[::-1])
    return str_s + str_r


def test():
    print "ADcv == Adcv: Not distinct=>", strcmp("ADcv", "Adcv", False)
    print "ADcv == Adcv: distinct=>", strcmp("ADcv", "Adcv")
    print "ispalindromic('abcd')=>", ispalindromic("abcs")
    print "ispalindromic('abcddcba')=>", ispalindromic("abcddcba")
    print "mkpalindromic('abcd')=>", mkpalindromic('abcd')


if __name__ == '__main__':
    test()
