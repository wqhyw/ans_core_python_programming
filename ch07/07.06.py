#! /usr/bin/env python

class data(object):
    def __init__(self):
        self.__col = ['stock ticker symbol', 'number of shares', 'purchase price', 'current price']
        self.__all = []
        self.__keys = set()
        self.__ch = 0
        self.__db = {}

    def __addstop(func):
        def stop(self):
            while True:
                func(self)
                ch = raw_input("\nEnd input?(y/n): ")
                if ch == 'y':
                    break
                elif ch == 'n':
                    continue
                else:
                    ch = raw_input("\nEnd input?(y/n): ")
        return stop

    def __addtoall(self, arow):
        self.__all.append(arow)

    @__addstop
    def __inpdata(self):
        while True:
            try:
                sts = raw_input("Input stock ticker symbol: ")
                nos = float(raw_input("Input number of shares: "))
                pp = float(raw_input("Input purchase price: "))
                cp = float(raw_input("Input current price: "))
            except ValueError:
                print 'Input error please tyr again'
            else:
                self.__addtoall([sts, nos, pp, cp])
                break

    def __sortall(self):
        promote = 'Which for sort key?\n' \
                  '0: Stock ticker symbol\n' \
                  '1: Number of shares\n' \
                  '2: Purchase price\n' \
                  '3: Current price\n'
        tryagin = '\nInput error, please try again.\n'
        while True:
            print promote
            try:
                ch = int(raw_input("Input your choice:"))
            except ValueError:
                print tryagin
            else:
                if ch < len(self.__all[0]):
                    self.__ch = ch
                    self.__all.sort(key=lambda data: data[ch])
                    for x in self.__all:
                        self.__keys.add(x[ch])
                    break
                else:
                    print tryagin

    def __setdb(self):
        if len(self.__keys) == len(self.__all):
            for x in self.__all:
                self.__db[x[self.__ch]] = x
        else:
            print self.__col[self.__ch], 'cannot be primary key'

    def getcol(self):
        return self.__col

    def setall(self):
        self.__inpdata()

    def getall(self):
        return self.__all

    def sortall(self):
        self.__sortall()

    def setdb(self):
        self.__setdb()

    def getdb(self):
        return self.__db


def main():
    d = data()
    d.setall()
    d.sortall()
    d.setdb()
    print d.getall()
    print d.getdb()

if __name__ == '__main__':
    main()
