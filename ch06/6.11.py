#! /usr/bin/env python

def ipcheck(ip, ctype=0):
    'Check that if string ip is valid'
    if ctype == 0:
        ip = ip.split('.')
        condition1 = (len(ip) == 4)
        condition2 = False not in [(x.isdigit() and 0 <= int(x) <= 255) for x in ip]
        return condition1 and condition2
    else:
        import string
        hexs = string.digits + string.letters[:6]
        for x in ip:
            if x not in hexs:
                return False
        else:
            return True


def iptobi(ip):
    "make a valid ip address which like www.xxx.yyy.zzz to binary integer"

    if ipcheck(ip):
        values = map(eval, ip.split('.'))
        ipint = ""

        for x in values:
            tmp = hex(x)[2:] + ' '
            ipint += '0' + tmp if len(tmp) < 3 else tmp
        return ipint
    else:
        return None


def bitoip(ip):
    'make a valid hex-integer to dotted decimal notation'

    if ipcheck(ip, 1):

        ip = int(ip, 16)
        if 0x0 <= ip <= 0xffffffff:
            result = []
            for x in xrange(4):
                result.append(str(ip % 0x100))
                ip //= 0x100

            return '.'.join(result[::-1])
        else:
            return None
    else:
        return None


def test():
    print iptobi(raw_input("dec: "))
    print bitoip(raw_input("hex-integer: "))


if __name__ == '__main__':
    test()
