#!/usr/local/bin/python3

'''
Authur:        Tarrell Fletcher
Date Created : December 16, 2016
Last Modified: December 20, 2016 16:01 
Email:         Tarrell13@verizon.net

Program will place items in the recycle bin instead of deleting them
Usage: ./recycle OPTIONS <File or Directory>
Options:
-v:             Verbose Output
-h, --help:     Show help menu with commands
--show-bin:     Show trash bin contents
--nuke:         Empty trash contents


Example: (1) ./recycle boo.txt
---------(2) ./recycle boo.txt foo.txt
---------(3) ./recycle dir
---------(4) ./recycle *.txt
'''

import os
import send2trash
import sys
import getopt


'''Check to see if user input is sufficient'''
def usage():
    print("Usage: ./recycle OPTIONS <Files or Directory>")
    print("Options: ")
    print("-v:          Verbose Output")
    print("-h, --help:  Show help menu")
    print("--show-bin:  Show trash bin contents")
    print("--nuke:      Empty trash bin contents(RUN ALONE)")
    print("")
    print("Example: (1) ./recycle boo.txt")
    print("---------(2) ./recycle boo.txt foo.txt")
    print("---------(3) ./recycle dir")
    print("---------(4) ./recycle *.txt")
    sys.exit()

commands = ["-h", "--help", "-v", "--show-bin", "--nuke"]

VERBOSE = False
MAC = False
LINUX = False
NUKE = False

'''Used to Get Command Line Options'''
def operations(arguments):

    global NUKE, VERBOSE

    try:
        getopt.getopt(arguments[1:], "h:v",["help", "show-bin", "nuke"])
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    for i in range(1, len(arguments)):
        if arguments[i] == ["-h", "--help"]:
            usage()
        elif arguments[i] == "--nuke":
            NUKE = True
        elif arguments[i] == "--show-bin":
            showBin()
        elif arguments[i] == "-v":
            VERBOSE = True


'''Checks to Determine Operating System'''
def systemCheck():
    global MAC, LINUX

    if os.uname()[0] == "Darwin":
        MAC = True
    elif os.uname()[0] == "Linux":
        LINUX = True
    else:
        print("System Unknown")


'''For verbose output'''
def success(file):
    location = '"'

    if MAC:
        location = "~/.Trash"
    elif LINUX:
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


'''Show trash bin contents'''
def showBin():
    print("------------------")
    print("Trash Bin Contents")
    print("------------------")
    if MAC:
        for file in os.listdir(os.path.expanduser("~") + "/.Trash"):
            if file == ".DS_Store":
                continue
            print("[+] %s" %file)
    elif LINUX:
        for file in os.listdir(os.path.expanduser("~")+"/.usr/local/Trash/files"):
            print("[+] %s" %file)
    else:
        print("Error")
    sys.exit()


'''Nuke the Trash Bin'''
def nuke():
    if MAC:
        os.system("rm -rf " + os.path.expanduser("~") + "/.Trash/*")
    elif LINUX:
        os.system("rm -rf " + os.path.expanduser("~") + "/.usr/local/Trash/files/*")
        os.system("rm -rf " + os.path.expanduser("~") + "/.usr/local/Trash/info/*")

    print("Trash Bin Emptied")
    sys.exit()


def main():

    systemCheck()
    operations(sys.argv)

    '''Displays help menu'''
    if len(sys.argv) < 2:
        usage()

    '''Checks for too many arguments when nuke or show-nin'''
    if len(sys.argv) >= 3 and NUKE:
        print("!!! Nuke must be run alone !!!")
    elif NUKE:
        nuke()
    else:
        multi_line(sys.argv)


main()
sys.exit()




