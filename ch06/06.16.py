#! /usr/bin/env python

def __matrixcheck(M):
    """
    @parogram: check if M a matrix
    @param: M => a list
    @return: True or False
    @rtype: bool
    """

    c = len(M[0])
    for x in M:
        if len(x) != c:
            return False
    else:
        return True


def __addcheck(M, N):
    """
    @parogram: check if M can be added by N
    @param: M, N => matrix
    @return: True or False
    @rtype: bool
    """

    if __matrixcheck(M) == False or __matrixcheck(N) == False:
        return False

    if len(M) == len(N) and type(M) == type([]) and type(N) == type([]):
        for x, y in zip(M, N):
            if len(x) != len(y) or type(x) != type([]) or type(N) != type([]):
                return False
        else:
            return True
    else:
        return False


def matrixadd(M, N):
    """
    @parogram: get summary of M, N
    @param: M, N => matrix
    @return: S => summary of M and N
    @rtype: list by list
    """

    if __addcheck(M, N):
        S = []
        for m, n in zip(M, N):
            r = []
            for x, y in zip(m, n):
                r.append(x + y)
            S.append(r)
        return S
    else:
        return -1


def __mulcheck(M, N):
    """
   @parogram: check if M can be multiply by N
   @param: M, N => matrix
   @return: True or False
   @rtype: bool
    """

    if __matrixcheck(M) and __matrixcheck(N):
        return len(M[0]) == len(N)
    else:
        return False


def matrixmul(M, N):
    """
    @parogram: get product of M, N
    @param: M, N => matrix
    @return: P => product of M and N
    @rtype: list by list
    """

    if __mulcheck(M, N):
        P = []
        for i in xrange(len(M)):
            P.append([])
            for j in xrange(len(N[0])):
                P[i].append(0)
                for k in xrange(len(N)):
                    P[i][j] += (M[i][k] * N[k][j])
        return P
    else:
        return -1


def test():
    # print __addcheck([[1], [3, 4]], [[5], [7, 8]])
    # print matrixadd([[1, 2], [2, 3]], [[5, 6], [7, 8]])
    # print matrixmul([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    # print matrixmul([[1, 1], [1, 1], [1, 1]], [[1, 1, 1], [1, 1, 1]])
    a = [[0.314, 0.507, 0.179]]
    b = [
        [0.1, 0.4, 0.5],
        [0.5, 0.3, 0.2],
        [0.4, 0.3, 0.3]
    ]
    print matrixmul(a, b)


if __name__ == '__main__':
    test()
