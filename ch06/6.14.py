#! /usr/bin/env python

from random import randint as ri


def getinp():
    """
    @program: get user's chioce
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
    @program: get computer's choice
    @return: 0 => rock, 1 => paper, 2 => scissors
    @rtype: int
    """

    return ri(0, 2)


def cmp(uinp, cinp):
    """
    @program: campare computer and user's choice
    @param: uinp => user input
    @param: cinp => computer input
    @return: 0 => user win
             1 => equal
             2 => computer win
    """

    cmplist = [[1, 0, 2], [2, 1, 0], [0, 2, 1]]
    return cmplist[uinp][cinp]


def main():
    """
    @program: main function
    """

    cinp = getinp()
    uinp = cominp()
    src = ['rock', 'paper', 'scissors']
    result = ['You win!', 'Equal', 'You lose']

    print "Your choice:", src[uinp]
    print "Computer's choice:", src[cinp]
    print result[cmp(uinp, cinp)]


if __name__ =='__main__':
    main()
