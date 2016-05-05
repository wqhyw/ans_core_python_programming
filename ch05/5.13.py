#! /usr/bin/env python

def hourtomin(timebyhour):
    """
    @program: make time like hour:minute to minute
    @param: time like hour:minute
    @tparam: string
    @rtype: int
    """
    time = timebyhour.split(':')
    return int(time[0]) * 60 + int(time[1])


def test():
    print hourtomin('2:10')


if __name__ == '__main__':
    test()
