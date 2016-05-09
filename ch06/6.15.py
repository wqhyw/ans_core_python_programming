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


def isleap(year):
    """
    @func: check leap or not
    @param: year
    @tparam: int
    @return: True or False
    @rtype: bool
    """

    condition1 = (year % 4 == 0) and (year % 100 != 0)
    condition2 = (year % 400 == 0)

    if condition1 or condition2:
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
        date1 = map(int, date1.split('/'))
        date2 = map(int, date2.split('/'))

        # date1 - date2 == (date1 - 01/01/1000) - (date2 - 01/01/1000)
        def __delt1000(date):
            """
            @program: get days form 01/01/1000
            @param: date
            @tparam: list by int
            @retrun: delta days
            @rtype: int
            """

            days = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
            daysleap = [32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
            delty = date[-1] - 1000
            deltd = delty // 4 * 1421 + delty % 4 * 365
            if isleap(date1[-1]):
                deltd += (days[date[-2]] + date[-3])
            else:
                deltd += (daysleap[date[-2]] + date[-3])

            return deltd

        return abs(__delt1000(date1) - __delt1000(date2))
    else:
        return -1


def getbirdelt():
    """
    @program: get user's birthday and calculate living days
    @return: days
    @rtype: int
    """

    import time

    while True:
        src = raw_input("Input your birthday(DD/MM/YYYY): ")
        if __datecheck(src):
            ts = time.strftime('%d/%m/%Y', time.localtime())
            return delt(src, ts)
        else:
            print "Invalid input."


def getnextbir():
    """
    @program: calculate next same day
    @return: days
    @rtype: int
    """
    while True:
        date = raw_input("Input your birthday(DD/MM/YYYY): ")
        if __datecheck(date):
            if re.match(r'29/02/\d{4}',date):
                return 1461
            else:
                return 365
        else:
            print "Invalid input."


def test():
    print delt('01/01/1995', '02/01/1995')
    print delt('18/10/1994', '07/05/2015')
    print delt('08/07/1995', '07/05/2015')
    print 'delt: ', delt('08/07/1995','01/11/1996')
    print delt('dfasfd', 'afd')
    print getbirdelt()
    print getnextbir()


if __name__ == '__main__':
    test()
