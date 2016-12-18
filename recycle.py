#!/usr/local/bin/python3

'''
Arthur:        Tarrell Fletcher
Date Created : December 16, 2016
Last Modified: December 17, 2016 03:38
Email:         Tarrell13@verizon.net

Program will place items in the recycle bin instead of deleting them
Usage: ./recycle OPTIONS <File or Directory>
Options:
-v:     Verbose Output

Example: (1) ./recycle boo.txt
---------(2) ./recycle boo.txt foo.txt
---------(3) ./recycle dir
---------(4) ./recycle *.txt
'''

import os
import send2trash
import sys

'''Check to see if user input is sufficient'''
if len(sys.argv) < 2:
    print("Usage: ./recycle OPTIONS <Files or Directory>")
    print("Options: ")
    print(" -v:     Verbose Output")
    print("")
    print("Example: (1) ./recycle boo.txt")
    print("---------(2) ./recycle boo.txt foo.txt")
    print("---------(3) ./recycle dir")
    print("---------(4) ./recycle *.txt")
    sys.exit()

commands = ["-v"]

VERBOSE = False

'''Turns command switches on'''
for i in range(1, len(sys.argv)):
    if sys.argv[i] in commands:
        if str(sys.argv[i]) == "-v":
            VERBOSE = True


def success(file):
    return "\"%s\" successfully sent to Trash :)" %file

'''Handle Multiple Command Line Files'''
def multi_line(arguments):
    for i in range(1,len(arguments)):
        try:
            if arguments[i] in commands:
                continue
            elif os.path.basename(arguments[i]) in os.listdir(os.getcwd()) or \
                 os.path.basename(arguments[i]) in os.listdir(os.path.dirname(arguments[i])):
                send2trash.send2trash(arguments[i])
                if VERBOSE:
                    print(success(arguments[i]))
            else:
                print("\"%s\" does not exist" % arguments[i])
        except FileNotFoundError:
            print("\"%s\" does not exist" %arguments[i])


multi_line(sys.argv)
sys.exit()

