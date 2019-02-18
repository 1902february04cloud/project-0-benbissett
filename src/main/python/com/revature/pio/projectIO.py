import sys
import os
from datetime import datetime

#Try users = dict(user) instead of for line loop
def getUsers():
    users = []
    with open('pio/users.txt', 'r') as user:
        for line in user:
            users.append(line.split())
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

def save(list):
    with open('pio/users.txt', 'w') as user:
        for line in list:
            user.write('{} {} {} \n'.format(line[0], line[1], line[2]))
    return True


