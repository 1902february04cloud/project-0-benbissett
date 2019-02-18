import sys
sys.path.append('../')
from service.projectService import *

def controller():
    running = True
    curr = False
    while running:
        while not curr:
            ip = input('Enter 1 to login or 2 to register or 3 to exit: ') 
            if ip == '1':
                curr = logIn()
            elif ip == '2':
                register()
            elif ip == '3':
                running = False
                curr = userSave()

        while curr and running:
            uinput = input('Enter 1 to check balance, 2 to withdraw, 3 to deposit, 4 to check history, 5 to log out: ')
            if uinput == '1':
                print(getBalance())
            elif uinput == '2':
                print(withdraw())
            elif uinput == '3':
                print(deposit())
            elif uinput == '4':
                transactions()
            elif uinput == '5':
                curr = logOut()
