import sys
import os
from datetime import datetime
sys.path.append('../')
from error.error import *

#checks if the users.txt file exists and if it does reads in all information in the file as a dictionary
def getUsers():
    users = dict()
    try:
        if os.path.exists('pio/users.txt'):
            with open('pio/users.txt', 'r') as user:
                data = user.read()
                users = dict(eval(data))
        else:
            raise(noUsersException)
    #handles error with no users have been registered to the bank
    except(noUsersException):
        print('No users registered so please create an account')
    finally:
        return users

#appends all transactions by user to the transactions.txt file to be read from later
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

#gets all of the transactions that the logged in user has ever done using grep on transactions.txt
def transactions(name):
    return os.system('grep {} "pio/transactions.txt"'.format(name))

#writes all the users in the user dictionary to a file to save them
def save(dic):
    with open('pio/users.txt', 'w') as user:
        user.write(str(dic))
    return True


