#! /usr/bin/env python

def getinp():
    'Get a valid integer'

    while True:
        inp = raw_input("Input an integer between 0 and 1000(boundary included): ")
        if inp.isdigit():
            return int(inp)
        else:
            print "Only integer is valid. Please try again."


def geteng(num):
    'Make num into english'

    # base words
    bases = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
        9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
        13: 'thirteen', 14: 'fouteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
        30: 'thirty', 40: 'fourty', 50: 'fifty', 60: 'sixty',
        70: 'seventy', 80: 'eighty', 90: 'ninety',
        0: 'zero', 1000: 'one thousand'
    }

    def handledozens(dozens):
        'handle integer between 10 - 99'

        if dozens in bases:
            if dozens != 0:
                return bases[dozens]
            else:
                return ''
        else:
            decade = (dozens // 10) * 10
            unit = dozens % 10
            return bases[decade] + '-' + bases[unit]

    if num in bases:
        return bases[num]
    else:
        # num < 1000 and num > 20 and num % 10 != 0

        hundreds = num // 100
        if hundreds != 0:
            dozens = num % 100
            isand = ' and ' if handledozens(dozens) != '' else ''
            return bases[hundreds] + ' hundred' + isand + handledozens(dozens)
        else:
            return handledozens(num)


def test():
    print geteng(getinp())


if __name__ == '__main__':
    test()
