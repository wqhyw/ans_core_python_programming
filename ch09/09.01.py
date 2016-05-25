#! /usr/bin/env python

def ignorecommnet(line):
    """
     @program: ignore comments after #
     @param: line => a line of a text file
     @return: res
     @rtype: string
    """

    res = line
    index = res.find('#')
    if index != -1:
        res = res[:index]
    return res


def main():
    f = open(r'../ch08/08.09.10.py', 'r')
    index = 0
    for line in f:
        index += 1
        line = ignorecommnet(line)
        if line != '':
            print index, ':', line,
        else:
            print index, ':'
    f.close()

if __name__ == '__main__':
    main()
