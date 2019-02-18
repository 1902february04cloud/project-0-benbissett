#!/usr/bin/env python3

from service.projectService import *

'''
This is your main testing script, this should call several other testing scripts on its own
'''
def main():
    with mock.patch('__builtin__.input', side_effect=['ben.bissett, password']):
        assert login() == True


if __name__ == '__main__':
	main()