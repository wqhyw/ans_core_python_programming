#! /usr/bin/env python

from random import randint as ri


def getinp():
    """
    @func: get user's chioce
    @return: 0 => rock, 1 => paper, 2 => scissors
    @rtype: int
    """

    while True:
        inp = raw_input("Input your choice(rock, paper, scissors): ")
        results = ['rock', 'paper', 'scissors']
        if inp in results:
            return results.index(inp)
        else:
            print "Invalid input"


def cominp():
    """
    @func: get computer's choice
    @return: 0 => rock, 1 => paper, 2 => scissors
    @rtype: int
    """

    return ri(0, 2)


def Rochambeau(uinp, cinp):
    """
    @func: campare computer and user's choice
    @param: uinp => user input
    @param: cinp => computer input
    @return: user win or deuce or computer win
    @rtype: string
    """

    cmplist = [[1, 0, 2], [2, 1, 0], [0, 2, 1]]
    result = ['You win!', 'Deuce', 'You lose!']
    return result[cmplist[uinp][cinp]]


def main():
    """
    @func: main function
    """

    uinp = getinp()
    cinp = cominp()
    src = ['rock', 'paper', 'scissors']

    print "Your choice:", src[uinp]
    print "Computer's choice:", src[cinp]
    print Rochambeau(uinp, cinp)


if __name__ =='__main__':
    main()
