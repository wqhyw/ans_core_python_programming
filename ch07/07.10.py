#! /usr/bin/env python

def rot13(source):
    """
    @program: rot13 program
    @param: source => to be en/decyrpt
    @return: result => string handled
    @rtype: string
    """

    result = []
    for x in source:
        asc = ord(x)
        if ord('a') <= asc <= ord('m') or ord('A') <= asc <= ord('M'):
            result.append(chr(asc+13))
        elif ord('n') <= asc <= ord('z') or ord('N') <= asc <= ord('Z'):
            result.append(chr(asc-13))
        else:
            result.append(x)
    result = ''.join(result)
    return result


def main():
    source = raw_input("Input your string to rot13: ")
    print "Your string is: [{src}]".format(src=source)
    result = rot13(source)
    print "The rot13 string is:[{res}]".format(res=result)


if __name__ == '__main__':
    main()
