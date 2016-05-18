#! /usr/bin/env python

def main():
    done = False
    begin = 0
    end = 0
    while not done:
        try:
            begin = int(raw_input("Enter begin value: "))
            end = int(raw_input("Enter end value: "))
            if begin > end:
                print "Begin cannot be bigger than end! Try again"
            else:
                done = True
        except (ValueError, TypeError):
            print "Invalid input! Try again."

    if 32 <= begin <= 128 or 32 <= end <= 128:
        print "DEC\tBIN\tOCT\tHEX\tASCII"
        print "- - - - - - - - - - -"
    else:
        print "DEC\tBIN\tOCT\tHEX"
        print "- - - - - - - - "

    for x in xrange(begin, end+1):
        d = str(x)
        b = '0'*(len(bin(end)[2:]) - len(bin(x)[2:])) + bin(x)[2:]
        o = oct(x)[1:]
        h = hex(x)[2:]

        out =  "{D}\t{B}\t{O}\t{H}\t".format(D=d, B=b, O=o, H=h)
        if 32 <= x <= 128: out += chr(x)
        print out


if __name__ == '__main__':
    main()
