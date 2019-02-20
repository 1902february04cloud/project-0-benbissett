import sys
import hashlib
from getpass import getpass
sys.path.append('../')
from pio.projectIO import *
from error.error import *
import logging
import logging.config
import yaml

#gets users from the file users.txt and save in a dict
#getUsers() is in projectIO.py in pio folder
users = getUsers()

if os.path.exists('service/logging.yaml'):
    with open('service/logging.yaml','r') as f:
        config = yaml.safe_load(f.read())
        #Enable our loaded configuration
        logging.config.dictConfig(config)
else:
    raise ValueError('Logging configuration not found')

logger = logging.getLogger('project-0')

#register users by asking for username and password and appending to users dict
def register():
    #logger.debug('Entring register function')
    name = input('Please enter your username: ')
    passW = getpass('Please enter your password: ')
    try:
        if name in users:
            #error if username is taken
            raise(duplicateNameException)
        else:
            #hash the password so that it is stored securely as a hash
            hasher = hashlib.sha1()
            hasher.update((passW).encode('utf-8'))
            hash = hasher.hexdigest()
            users[name] = [hash, '0']
    #handle username being taken and print a message to stdout and log error
    except(duplicateNameException):
        print('Username is already taken please use another')
        #logger.error('Username already taken')
    #finally:
        #logger.debug('Exiting register function')

#check if username and password is a valid user in users.txt and log them in if they are
def logIn():
    userName = ""
    #logger.debug('Entering login function')
    try:
        name = input('Please enter your username: ')
        value = users.get(name)
        passW = getpass('Please enter your password: ')
        #raise and error if username not in user dict
        if not value:
            #logger.error('Invalid username entered')
            raise(logInException)
        hasher = hashlib.sha1()
        hasher.update((passW).encode('utf-8'))
        hash = hasher.hexdigest()
        if value[0] == hash:
            userName = name
            print('Logged in successfully')
            return userName
        #raise and error if password hashes don't match
        else:
            #logger.error('Invalid password entered for {}'.format(name))
            raise(logInException)
    #handle if username or password were incorrect
    except(logInException):
        print('Username or password were incorrect')
        return userName
    #finally:
        #logger.debug('Exiting login function')

#returns the balance of the user with userName
def getBalance(userName):
    value = users.get(userName)
    return value[1]

#prints out a message telling user how much money is in the account and logs a transaction
def checkBalance(userName):
    #logging.debug('Entering checkBalance function')
    writeToTransaction(0, userName, 0)
    balance = getBalance(userName)
    #logging.debug('Exiting checkBalance function')
    return 'Your have ${} remaining in your account'.format(balance)

#allows user to withdraw money from account as long as amount entered is less than the money in the account
#records a withdraw transaction in the users name
def withdraw(userName):
    #logging.debug('Entering withdraw function')
    #makes sure the amount to be withdrawn is a valid number and not a string
    try:
        amount = float(input('Enter the amount you would like to withdraw: '))
    except(ValueError):
        #logging.error('Entered a string instead of a valid numerical number')
        return 'Unable to complete transaction please enter a valid number'
        
    balance = float(getBalance(userName))
    try:
        #raises an error if there isn't enough money in account to handle withraw request
        if balance <= 0 or amount > balance:
            raise(notEnoughMoneyException)
        else:
            balance -= amount
            #format the floats to have 2 decimal places
            balance = '{0:.2f}'.format(round(balance,2))
            amount = '{0:.2f}'.format(round(amount,2))
            value = users.get(userName)
            users[userName] = [value[0], balance]
            writeToTransaction(1, userName, amount)
            #logging.debug('Exiting withdraw function')
            return 'Your have withdrawn ${} leaving you with ${}'.format(amount, balance)
    #handles not enough money and prints out a message
    except(notEnoughMoneyException):
        #logging.error('Not enough money in account for withdraw')
        return 'Not enough money in account to complete transaction.'

#allows person logged in to deposit money into their account and records a transaction in users name
def deposit(userName):
    #logging.debug('Entering deposit function')
    #checks if the input is a valid number otherwise handles the error
    try:
        amount = float(input('Enter the amount you would like to deposit: '))
    except(ValueError):
        #logging.error('Entered a string instead of a valid numerical value')
        return 'Unable to complete transaction please enter a valid number'
    balance = float(getBalance(userName))
    balance += amount
    #same formatting as withdraw
    balance = '{0:.2f}'.format(round(balance,2))
    amount = '{0:.2f}'.format(round(amount,2))
    value = users.get(userName)
    users[userName] = [value[0], balance]
    writeToTransaction(2, userName, amount)
    #logging.debug('Exiting deposit function')
    return 'You have deposited ${} leaving you with ${}'.format(amount, balance)

#calles transactions in projectIO to get all the transactions that have been done by the logged in user
def getTransactions(userName):
    #logging.debug('Entered transactions method')
    #logging.debug('Excited transactions method')
    return transactions(userName)

#log out and allow more people to logIn or register
def logOut():
    return False

#calls the save(users) in projectIO
#saves all user information to be used next time program started and only called on program shutdown
def userSave():
    return save(users)
