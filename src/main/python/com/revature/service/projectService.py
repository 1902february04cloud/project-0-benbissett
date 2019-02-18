import sys
sys.path.append('../')
from pio.projectIO import *

userIndex = 0
users = getUsers()

def getUser():
    name = input('Please enter your username: ')
    passW = input('Please enter your password: ')
    return [name, passW]

def register():
    account = getUser()
    users.append([str(account[0]), str(account[1]), 0.00])

def logIn():
    global userIndex
    account = getUser()
    for user in users:
        if str(account[0]) == str(user[0]) and str(account[1]) == str(user[1]):
            userIndex = users.index(user)
            print('Logged in successfully')
            return True
    print('Username or password were incorrect')
    return False

def getBalance():
    return users[userIndex][2]

def checkBalance():
    writeToTransaction(0, users[userIndex][0], 0)
    return 'Your have ${} remaining in your account'.format(getBalance())

def withdraw():
    amount = float(input('Enter the amount you would like to withdraw: '))
    balance = float(getBalance())
    if balance <= 0 or amount > balance:
        return 'Cannot withdraw because balance is too low'
    else:
        balance -= amount
        users[userIndex][2] = str(balance)
        writeToTransaction(1, users[userIndex][0], amount)
        return 'Your have withdrawn ${} leaving you with ${}'.format(amount, balance)

def deposit():
    amount = float(input('Enter the amount you would like to deposit: '))
    balance = float(getBalance())
    balance += amount
    users[userIndex][2] = str(balance)
    writeToTransaction(2, users[userIndex][0], amount)
    return 'You have deposited ${} leaving you with ${}'.format(amount, balance)

def transactions():
    return transactions(users[userIndex][0])

def logOut():
    return False

def userSave():
    return save(users)
