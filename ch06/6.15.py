#! /usr/bin/env python

import re

def __datecheck(date):
    """
    @func: check if date valid
    @param: date => a string
    @return: Ture => date like DD/MM/YYYY
            False => not valid date
    @rtype: bool
    """

    # A RE to match valid date.
    # I don't understand too.
    pattern = r"(((0[1-9]|[12][0-9]|3[01])/((0[13578]|1[02]))|" \
              r"((0[1-9]|[12][0-9]|30)/(0[469]|11))|(0[1-9]|[1][0-9]|2[0-8])" \
              r"/(02))/([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}" \
              r"|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3}))|(29/02/" \
              r"(([0-9]{2})(0[48]|[2468][048]|[13579][26])" \
              r"|((0[48]|[2468][048]|[3579][26])00)))"

    if re.match(pattern, date):
        return True
    else:
        return False


def delt(date1, date2):
    """
    @func: calculate delta between date1 and date2
    @param: date1, date2 => two date string like DD/MM/YYYY
    @return: days, -1 when params invalid
    @rtype: int
    """

    if __datecheck(date1) and __datecheck(date2):
        pass #TODO
    else:
        return -1


def test():
    print __datecheck('02/03/2015')
    print __datecheck('29/02/2015')
    print __datecheck('28/02/2015')
    print __datecheck('asda')


if __name__ == '__main__':
    test()
