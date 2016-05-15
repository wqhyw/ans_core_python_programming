#! /usr/bin/env python

def ipcheck(ip, ctype=0):
    """
    @func: Check that if string is a valid ip
    @param: ctype == 0 then ip => an ip address like www.xxx.yyy.zzz
            ctype != 0 then ip => a hex-integer
    @return: True for valid, False for invalid

    """

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
    """
    @func: make an ip address in dotted decimal notation to a hex-integer
    @param: ip => an ip address in dotted decimal notation
    @tparam: string
    @return: ipint => a hex-integer
             None => when param invalid
    @rtype: string
    """

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
    """
    @func: make a hex-integer to an ip address in dotted decimal notation
    @param: ip => a hex-integer
    @tparam: string
    @return: None => when param invalid
             ip address in dotted decimal notation
    @rtype: string
    """

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
