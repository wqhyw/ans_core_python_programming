#! /usr/bin/env python

def ipcheck(ip):
    'Check that if string ip is valid'
    ip = ip.split('.')
    condition1 = (len(ip) == 4)
    condition2 = False not in [(x.isdigit() and 0 <= int(x) <= 255) for x in ip]
    return condition1 and condition2


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
        return  None


def bitoip(ip):
    "make a valid integer to ip address like www.xxx.yyy.zzz"

    result = []
    if ip < 0 or ip > 0xffffffff:
        return None
    else:
        # TODO
        pass


def test():
    print iptobi(raw_input("dec: "))
    print bitoip(int(raw_input("integer: ")))


if __name__ == '__main__':
    test()
