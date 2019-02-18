import sys
import os
from datetime import datetime
sys.path.append('../')
from error.error import *

def getUsers():
    users = dict()
    try:
        if os.path.exists('pio/users.txt'):
            with open('pio/users.txt', 'r') as user:
                data = user.read()
                users = dict(eval(data))
        else:
            raise(noUsersException)
    except(noUsersException):
        print('No users registered so please create an account')
    finally:
        return users

def writeToTransaction(number, name, amount):
    if number == 0:
        with open('pio/transactions.txt', 'a+') as trans:
            trans.write('{} checked balance at {} \n'.format(str(name), datetime.now()))
    elif number == 1:
        with open('pio/transactions.txt', 'a+') as trans:
            trans.write('{} withdrew ${} at {} \n'.format(str(name), str(amount), datetime.now()))
    else:
        with open('pio/transactions.txt', 'a+') as trans:
            trans.write('{} deposited ${} at {} \n'.format(str(name), str(amount), datetime.now()))

def transactions(name):
    return os.system('grep {} "pio/transactions.txt"'.format(name))

def save(dic):
    with open('pio/users.txt', 'w') as user:
        user.write(str(dic))
    return True


