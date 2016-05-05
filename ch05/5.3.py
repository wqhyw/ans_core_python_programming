#! /usr/bin/env python

def getegrade(score):
    """
    @program: get grade
    @param: score
    @tparam: int
    @return: A or B or C or D or E
    @rtype: char
    """

    if score < 0 or score > 100:
        return None
    elif score <= 100 and score >= 90:
        return 'A'
    elif score >=80:
        return 'B'
    elif score >=70:
        return 'C'
    elif score >=60:
        return 'D'
    else:
        return 'E'


def test():
    print getegrade(75)

if __name__ == '__main__':
    test()