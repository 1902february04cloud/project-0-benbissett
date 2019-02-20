#!/usr/bin/env python3

import unittest
from service.projectService import *

'''
This is your main testing script, this should call several other testing scripts on its own
'''
def main():
    #test if deposit works correctly when given a number as an imput or a string as an input
    with mock.patch('builtins.input', side_effect=['100']):
        assert deposit('paul') == 'You have deposited $100.00 leaving you with $200.00'
    with mock.patch('builtins.input', side_effect=['abd']):
        assert deposit('paul') == 'Unable to complete transaction please enter a valid number'
    #tests if withdraw works correctly when asked to withdraw a string, too much money or a correct amount
    with mock.patch('builtins.input', side_effect=['abd']):
        assert withdraw('paul') == 'Unable to complete transaction please enter a valid number'
    with mock.patch('builtins.input', side_effect=['100']):
        assert withdraw('paul') == 'You have withdrawn $100.00 leaving you with $100.00'
    with mock.patch('builtins.input', side_effect=['1000']):
        assert withdraw('paul') == 'Not enough money in account to complete transaction.'
    

if __name__ == '__main__':
	main()