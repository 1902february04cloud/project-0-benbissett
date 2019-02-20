import sys
sys.path.append('../')
from service.projectService import *

def controller():
    running = True
    curr = False
    userName = ""
    #lopps over the login in register or exit part of the code
    #if you exit the program ends and saves all users to a text file
    while running:
        while not curr:
            ip = input('Enter 1 to login or 2 to register or 3 to exit: ') 
            if ip == '1':
                userName = logIn()
                if userName != '':
                    curr = True
            elif ip == '2':
                register()
            elif ip == '3':
                running = False
                curr = userSave()
        #if logged in loops over the check balance, withdraw, deposit, check transactions, or log out
        #when you log out it goes back to looping over login and register
        while curr and running:
            uinput = input('Enter 1 to check balance, 2 to withdraw, 3 to deposit, 4 to check history, 5 to log out: ')
            if uinput == '1':
                print(checkBalance(userName))
            elif uinput == '2':
                print(withdraw(userName))
            elif uinput == '3':
                print(deposit(userName))
            elif uinput == '4':
                getTransactions(userName)
            elif uinput == '5':
                curr = logOut()
