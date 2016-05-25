#! /usr/bin/env python

import certificate_of_deposit
import checkings
import savings
import money_market
import functions


def menu(promote, ** callbacks):
    """
    @program: a template of menu interface
    @param: promote => menu information
             callbacks => dict params, key=choice, value=function
    """

    print promote
    done = False
    while not done:
        cho = raw_input("Enter your choice: ")
        print "You choosed [{ch}]\n".format(ch=cho[0])
        if cho[0] in callbacks.keys():
            callbacks[cho[0]]()
        elif cho[0] == 'r':
            done = True
        else:
            print "Invalid choice, reenter please."


def savings_menu():
    promote = """
*************************
      Savings
*************************
a. add_deposit
b. add_withdrawal
c. show_remains
d. show_all_records
e. show_deposit_records
f. show_withdrawal_records
u. undo
r. back
"""
    callbacks = dict(a=savings.add_deposit,
                     b=savings.add_withdrawal,
                     c=savings.show_remains,
                     d=savings.show_all_records,
                     e=savings.show_deposit_records,
                     f=savings.show_withdrawal_recors,
                     u=savings.undo,
                     r=savings.back)

    menu(promote, **callbacks)

def checkings_menu():
    promote = """
*************************
      Checkings
*************************
a. add_in
b. add_out
c. show_remains
d. show_in_records
e. show_out_records
u. undo
r. back
"""
    callbacks = dict(a=checkings.add_in,
                     b=checkings.add_out,
                     c=checkings.show_remains,
                     d=checkings.show_in_records,
                     e=checkings.show_out_records,
                     u=checkings.undo,
                     r=checkings.back)
    menu(promote, **callbacks)


def money_market_menu():
    promote = """
*************************
      Money Market
*************************
a. add_invest
b. show_all_out
c. show_earns
u. undo
r. back
"""
    callbacks = dict(a=money_market.add_invest,
                     b=money_market.show_all_out,
                     c=money_market.show_earns,
                     u=money_market.undo,
                     r=money_market.back)

    menu(promote, **callbacks)


def CD_menu():
    promote = """
*************************
 Certificate of Deposit
*************************
a. add_deposit
b. show_deposits
c. show_records
u. undo
r. back
"""
    callbacks = dict(a=certificate_of_deposit.add_deposit,
                     b=certificate_of_deposit.show_deposits,
                     c=certificate_of_deposit.show_records,
                     u=certificate_of_deposit.undo,
                     r=certificate_of_deposit.back)

    menu(promote, **callbacks)


def functions_menu():
    promote = """
*************************
      Functions
*************************
a. show_wealth
b. save
u. clear
r. quit
"""
    callbacks = dict(a=functions.show_wealth,
                     b=functions.save,
                     c=functions.clear,
                     r=functions.quit)

    menu(promote, **callbacks)


def main_menu():
    promote = """
*************************
          Menu
*************************
a. saving_menu
b. checking_menu
c. money_market_menu
d. CD_menu
e. functions
r. exit
"""
    callbacks = dict(a=savings_menu,
                     b=checkings_menu,
                     c=money_market_menu,
                     d=CD_menu,
                     e=functions_menu,
                     r=exit_)

    menu(promote, **callbacks)


def exit_():
    pass


def do():
    print "do called."
