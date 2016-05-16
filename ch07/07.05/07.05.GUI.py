# coding=utf-8
from Tkinter import *
from datetime import *

class USPGUI(object):
    def __init__(self):
        self.__init_properties()
        self.__init_root()
        self.__init_menu()
        self.__init_labels()
        self.__init_entrys()
        self.__init_buttons()
        self.__layout()

    def __init_properties(self):
        self.__db = {}
        self.__session = {}
        self.__history = {}

    def __init_root(self):
        self.root = Tk()
        self.root.resizable(False, False)
        self.root.title('GUI1.0')
        self.root.iconbitmap('ICO.ico')

    def __init_menu(self):
        self.menubar = Menu(self.root)
        self.mnmenu = Menu(self.menubar, tearoff=0)
        self.mnmenu.add_command(label='Register', command=lambda : self.__changebut('register'))
        self.mnmenu.add_separator()
        self.mnmenu.add_command(label='Login', command=lambda : self.__changebut('login'))
        self.mnmenu.add_command(label='Logout', command=self.__logout)
        self.mnmenu.add_separator()
        self.mnmenu.add_command(label='ShowAll', command=self.__showall)
        self.mnmenu.add_command(label='DeleteUser', command=lambda : self.__changebut('delete'))
        self.menubar.add_cascade(label='Manage', menu=self.mnmenu)
        self.menubar.add_command(label='Exit', command=self.root.quit)
        self.root.config(menu=self.menubar)

    def __init_labels(self):
        self.stateLabel = Label(self.root, text='No User logged in.')
        self.usrNameLabel = Label(self.root, text='UserName:')
        self.pwdLabel = Label(self.root, text='Password:')

    def __init_entrys(self):
        self.__name = StringVar()
        self.__pwd = StringVar()
        self.nameEntry = Entry(self.root, bg='lightgrey', textvariable=self.__name)
        self.pwdEntry = Entry(self.root, bg='lightgrey', textvariable=self.__pwd, show='*')

    def __init_buttons(self):
        self.loginBut = Button(self.root, text='Login', width=8, command=self.__login)
        self.clearBut = Button(self.root, text='Clear', width=8, command=self.__clear)

    def __layout(self):
        self.stateLabel.grid(row=0, column=0, columnspan=3, pady=6, sticky=N)
        self.usrNameLabel.grid(row=1, column=0, pady=2, sticky=W)
        self.nameEntry.grid(row=1, column=1, columnspan=2, padx=3, pady=2)
        self.pwdLabel.grid(row=2, column=0, pady=2)
        self.pwdEntry.grid(row=2, column=1, columnspan=2, padx=3, pady=2)
        self.loginBut.grid(row=3, column=1, pady=5)
        self.clearBut.grid(row=3, column=2, pady=5)

    def __register(self):
        name = (self.__name.get()).lower()
        pwd = self.__pwd.get()
        if self.__namecheck(name):
            if name in self.__db:
                self.__msgbox("Username token, please try another one!")
            else:
                if name == '' or pwd == '':
                    self.__msgbox("Please input!")
                else:
                    self.__db[name]=pwd
                    self.__msgbox("Register done!")
                    self.__clear()
        else:
            self.__msgbox("Username invalid! Only letters valid!")

    def __login(self):
        name = (self.__name.get()).lower()
        pwd = self.__pwd.get()
        if len(self.__session) == 1:
            self.__msgbox("Please logout before login! ")
        else:
            if name in self.__db:
                if self.__db[name] == pwd:
                    now = datetime.now()
                    self.__session[name] = now
                    if name in self.__history:
                        his  = self.__history[name]
                        delt = (now - his).seconds
                        print his, now, delt
                        if delt < 14400:
                            self.__msgbox("Your have logged in {time}".format(time=str(his)[:19]))
                    self.__msgbox("Welcome {name}!".format(name=name))
                    self.__history[name] = datetime.now()
                    self.stateLabel.config(text="Now: {fn}.".format(fn=name))
                else:
                    self.__msgbox("Password incorrect! Please try again. ")
            else:
                self.__msgbox("User don't exists! Please try again. ")
        self.__clear()

    def __logout(self):
        if len(self.__session) == 0:
            self.__msgbox("No one logged!")
        else:
            self.__msgbox("Bye Bye!")
            self.__session.clear()
            self.stateLabel.config(text='No User logged in.')

    def __deleteusr(self):
        if len(self.__session) == 0:
            self.__msgbox("Please login first!")
        else:
            name = (self.__name.get()).lower()
            pwd = self.__pwd.get()
            if name in self.__db:
                if name in self.__session:
                    self.__msgbox("Cannot delete yourself, please try again!")
                else:
                    if self.__db[name] == pwd:
                        del self.__db[name]
                        self.__msgbox("Delete {name} done!".format(name=name))
                    else:
                        self.__msgbox("Password incorrect! Please try again. ")
            else:
                self.__msgbox("User don't exists! Please try again. ")
            self.__clear()

    def __showall(self):
        all = []
        for k,v in self.__db.items(): all.append(k)
        promote = ' '.join(all)
        promote = "All users below:\n" + promote
        self.__msgbox(promote)

    def __clear(self):
        self.__name.set('')
        self.__pwd.set('')
        print self.__history

    def __changebut(self, butname):
        funcs = dict(register=self.__register, login=self.__login, delete=self.__deleteusr)
        promotes = dict(register="Input your name and password to register!",
                        login="Input your name and password to login!",
                        delete="Input name to delete, password to ensure!")
        self.loginBut.config(text=butname.title(), command=funcs[butname])
        self.__msgbox(promotes[butname])

    @staticmethod
    def __msgbox(promote):
        msg = Toplevel()
        msg.iconbitmap('ICO.ico')
        msg.resizable(False, False)
        msgLabel = Label(msg, text=promote)
        okbut = Button(msg, text='OK', width=10, command=msg.withdraw)
        msgLabel.pack(pady=2)
        okbut.pack(pady=2)

    @staticmethod
    def __namecheck(name):
        for x in name:
            if ord('a') >= ord(x) or ord(x) >= ord('z'):
                return False
        else:
            return True

def main():
    a = USPGUI()
    a.root.mainloop()

if __name__ == '__main__':
    main()
