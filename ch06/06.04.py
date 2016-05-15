#! /usr/bin/env python

def getgrade(score):
    """
    @func: get grade by score
    @param: score
    @tparam: int
    @return: grade in A,B,C,D,E
    @rtype: char
    """

    if score < 0 or score > 100:
        return None
    else:
        grade = ['A', 'B', 'C', 'D', 'E']
        if score == 100:
            return  grade[0]
        elif score >= 60:
            return grade[9 - score / 10]
        else:
            return grade[4]


def test():
    import random
    rns = random.randint(1, 100)
    print rns, '=>', getgrade(rns)


if __name__ == '__main__':
    test()
