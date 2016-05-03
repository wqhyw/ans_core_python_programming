# ! /usr/bin/env python

def hourtomin(timebyhour):
    time = timebyhour.split(':')
    return int(time[0]) * 60 + int(time[1])


def test():
    print hourtomin('2:10')


if __name__ == '__main__':
    test()
