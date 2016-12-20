#!/usr/local/bin/python3

'''
Authur:        Tarrell Fletcher
Date Created : December 16, 2016
Last Modified: December 17, 2016 03:38
Email:         Tarrell13@verizon.net

Program will place items in the recycle bin instead of deleting them
Usage: ./recycle OPTIONS <File or Directory>
Options:
-v:             Verbose Output
-h, --help:     Show help menu with commands
--show-bin:     Show trash bin contents
--empty:        Empty trash contents


Example: (1) ./recycle boo.txt
---------(2) ./recycle boo.txt foo.txt
---------(3) ./recycle dir
---------(4) ./recycle *.txt
'''

import os
import send2trash
import sys

'''Check to see if user input is sufficient'''
def usage():
    print("Usage: ./recycle OPTIONS <Files or Directory>")
    print("Options: ")
    print(" -v:         Verbose Output")
    print("-h, --help:  Show help menu")
    print("--show-bin:  Show trash bin contents(RUN ALONE)")
    print("--empty:     Empty trash bin contents(RUN ALONE)")
    print("")
    print("Example: (1) ./recycle boo.txt")
    print("---------(2) ./recycle boo.txt foo.txt")
    print("---------(3) ./recycle dir")
    print("---------(4) ./recycle *.txt")
    sys.exit()

commands = ["-v", "-h", "--help", "--show-bin", "--empty"]

VERBOSE = False
MAC = False
LINUX = False

'''Checks to Determine Operating System'''
def systemCheck():
    if os.uname()[0] == "Darwin":
        MAC = True
    elif os.uname()[0] == "Linux":
        LINUX = True

'''Turns command switches on'''
def switchOn(arguments):
    for i in range(1, len(arguments)):
        if arguments[i] in commands:
            if str(arguments[i]) == "-v":
                VERBOSE = True


def success(file):

    location = '"'

    if os.uname()[0] == "Darwin":
        location = "~/.Trash"
    elif os.uname()[0] == "Linux":
        location = "~/.local/share/Trash"
    return "\"%s\" successfully sent to %s" %(file, location)

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


'''Some commands can only be run if they are Specified Alone!'''
def sanity(arguments):
    if len(arguments) == 2:
        return True
    else:
        print("!!!Command:\"%s\" must be run alone!!!")
        sys.exit()


'''Show trash bin contents'''
def showBin():
    print("------------------")
    print("Trash Bin Contents")
    print("------------------")
    if MAC:
        for file in os.listdir(os.environ["HOME"]+"/.Trash"):
            if file == ".DS_Store":
                continue
            print("[+] %s" %file)
    elif LINUX:
        for file in os.listdir(os.environ["HOME"]+"/.usr/local/files"):
            print("[+] %s" %file)
    else:
        print("Error")


#multi_line(sys.argv)

systemCheck()
showBin()
sys.exit()

