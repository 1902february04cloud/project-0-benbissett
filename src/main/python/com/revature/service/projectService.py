import sys
import hashlib
from getpass import getpass
sys.path.append('../')
from pio.projectIO import *
from error.error import *
import logging
import logging.config
import yaml

userName = ""
users = getUsers()
if os.path.exists('logging.yaml'):
        with open('logging.yaml','r') as f:
            config = yaml.safe_load(f.read())
        #Enable our loaded configuration
        logging.config.dictConfig(config)
else:
    raise ValueError('Logging configuration not found')

logger = logging.getLogger('project-0')

def register():
    logger.debug('Entring register function')
    name = input('Please enter your username: ')
    passW = getpass('Please enter your password: ')
    try:
        if name in users:
            raise(duplicateNameException)
        else:
            hasher = hashlib.sha1()
            hasher.update((passW).encode('utf-8'))
            hash = hasher.hexdigest()
            users[name] = [hash, '0']
    except(duplicateNameException):
        print('Username is already taken please use another')
        logger.error('Username already taken')
    finally:
        logger.debug('Exiting register function')

def logIn():
    global userName
    logger.debug('Entering login function')
    try:
        name = input('Please enter your username: ')
        value = users.get(name)
        passW = getpass('Please enter your password: ')
        if not value:
            logger.error('Invalid username entered')
            raise(logInException)
        hasher = hashlib.sha1()
        hasher.update((passW).encode('utf-8'))
        hash = hasher.hexdigest()
        if value[0] == hash:
            userName = name
            print('Logged in successfully')
            return True
        else:
            logger.error('Invalid password entered for {}'.format(name))
            raise(logInException)
    except(logInException):
        print('Username or password were incorrect')
        return False
    finally:
        logger.debug('Exiting login function')

def getBalance():
    value = users.get(userName)
    return value[1]

def checkBalance():
    logging.debug('Entering checkBalance function')
    writeToTransaction(0, userName, 0)
    balance = getBalance()
    logging.debug('Exiting checkBalance function')
    return 'Your have ${} remaining in your account'.format(getBalance())

def withdraw():
    logging.debug('Entering withdraw function')
    try:
        amount = float(input('Enter the amount you would like to withdraw: '))
    except(ValueError):
        logging.error('Entered a string instead of a valid numerical number')
        return 'Unable to complete transaction please enter a valid number'
        
    balance = float(getBalance())
    try:
        if balance <= 0 or amount > balance:
            raise notEnoughMoneyException()
    except(notEnoughMoneyException()):
        logging.error('Not enough money in account for withdraw')
        print('Not enough money in account to complete transaction.')
    else:
        balance -= amount
        balance = '{0:.2f}'.format(round(balance,2))
        amount = '{0:.2f}'.format(round(amount,2))
        value = users.get(userName)
        users[userName] = [value[0], balance]
        writeToTransaction(1, userName, amount)
        logging.debug('Exiting withdraw function')
        return 'Your have withdrawn ${} leaving you with ${}'.format(amount, balance)

def deposit():
    logging.debug('Entering deposit function')
    try:
        amount = float(input('Enter the amount you would like to deposit: '))
    except(ValueError):
        logging.error('Entered a string instead of a valid numerical value')
        return 'Unable to complete transaction please enter a valid number'
    balance = float(getBalance())
    balance += amount
    balance = '{0:.2f}'.format(round(balance,2))
    amount = '{0:.2f}'.format(round(amount,2))
    value = users.get(userName)
    users[userName] = [value[0], balance]
    writeToTransaction(2, userName, amount)
    logging.debug('Exiting deposit function')
    return 'You have deposited ${} leaving you with ${}'.format(amount, balance)

def transactions():
    logging.debug('Entered transactions method')
    logging.debug('Excited transactions method')
    return transactions(users[userIndex][0])

def logOut():
    return False

def userSave():
    return save(users)
