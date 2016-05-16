#!/usr/bin/env python
# TODO: GUI

import hashlib

db = {}
logtime = {}

def newuser():

    """
    @program: create a new user
    """
    prompt = 'login desired: '
    while True:
        name = raw_input(prompt)
        if db.has_key(name):
            prompt = 'name taken, try another: '
        else:
            break
    pwd = raw_input('passwd: ')

    import hashlib
    db[name] = hashlib.new('md5', pwd).hexdigest()


def olduser():
    """
    @program: login and add timestamp
    """

    name = raw_input('login: ')
    if name not in db:
        print 'user do not exists.'
        return

    pwd = raw_input('passwd: ')
    pwd = hashlib.new('md5', pwd).hexdigest()
    passwd = db.get(name)
    if passwd == pwd:
        print 'welcome back', name

        import datetime
        if name in logtime:
            now = datetime.datetime.now()
            past = logtime.get(name)
            delt = (now - past).seconds

            if delt < 14400:
                print 'You have already logged in at: %s' % str(now)[:19]

        logtime[name] = datetime.datetime.now()
    else:
        print 'login incorrect'


def manage():
    """
    @program: print user information and delete user
    """
    prompt = "(p)rint users\n" \
             "(d)elete user\n" \
             "(b)back\n\n" \
             "Enter choice: "

    while True:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt)[0]
            except (EOFError, KeyboardInterrupt):
                choice = 'b'
            print '\nYou picked: [%s]' % choice

            if choice not in 'pdb':
                print 'invalid menu option, try again'
            else:
                chosen = True

        if choice == 'p':
            print 'All users:',
            for x in db.keys():
                print x
            print

        elif choice == 'd':
            dn = raw_input('name you want to delete: ')
            if dn in db:
                pwd = raw_input('input password to ensure:')
                if pwd == db.get(dn):
                    del db[dn]
                    print '%s has deleted.' % dn
                else:
                    print 'password incorrect, delete failed.'
            else:
                print '%s not exists.'

        elif choice == 'b': break

    showmenu()


def showmenu():
    """
    @program: print menu and handle choices
    """
    prompt = "\n(n)ew User Login\n" \
             "(e)xisting User Login\n" \
             "(m)anage users\n" \
             "(q)uit\n\n" \
             "Enter choice: "

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt)[0]
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked: [%s]' % choice

            if choice not in 'neqm':
                print 'invalid menu option, try again'
            else:
                chosen = True

        if choice == 'q': done = True
        if choice == 'n': newuser()
        if choice == 'm': manage()
        if choice == 'e': olduser()


if __name__ == '__main__':
    showmenu()
