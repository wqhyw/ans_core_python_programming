#! /usr/bin/env python

# get all files of python standard library
# from os import walk as ls
# from os.path import join as jn
#
# def getstd():
#     """
#     @program: get all modules in python standard libs
#     @return: pys => module names and full path
#     @rtype: dict
#     """
#     root = r'C:\MyApps\py2.7\Lib'
#     full = ls(root)
#     match = getattr(__import__('re'), 'match')
#     pys = dict()
#     for parent, dirs, files in full:
#         for fi in files:
#             if match(r'\w+\.py', fi):
#                 pys[fi.split('.')[0]] = jn(parent, fi)
#
#     return pys


def getdoc(modname, docname):
    """
    @program: get all doc strings of modname into docname
    @param: modname => name of py module
            docname => name of doc file
    @return: True for succeed, False for failed
    @rtype: bool
    """
    try:
        mod = __import__(modname)
        f = open(docname, 'w')
        splitline = "\n" + '*-' * 30 + "*\n"
        f.write(mod.__name__+":\n")
        f.write(reformatdoc(mod.__doc__))
        d = mod.__dict__
        for x in d:
            doc = x.__doc__
            f.write(splitline)
            f.write(x+": ")
            f.write(str(type(getattr(mod, x))))
            f.write('\n')
            f.write(reformatdoc(x.__doc__))
        f.close()
    except (ImportError, IOError), e:
        print e
        return False
    else:
        return True


def reformatdoc(doc):
    """
    @program: add tabs to __doc__ string
    @param: doc => a __doc__ string
    @return: res
    @rtype: string
    """

    res = ''
    lines = doc.split('\n')
    for line in lines:
        res += ' '*4 + line + '\n'

    return res

if __name__ == '__main__':
    getdoc('re', 'docs/re_doc.txt')
