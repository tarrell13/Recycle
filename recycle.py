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
--nuke:         Empty trash contents


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


'''Commands'''
commands = ["-v", "-h", "--help", "--show-bin", "--nuke"]

VERBOSE = False
MAC = False
LINUX = False
NUKE = False
#SHOWBIN = False





'''Checks to Determine Operating System'''
def systemCheck():
    global MAC, LINUX

    if os.uname()[0] == "Darwin":
        MAC = True
    elif os.uname()[0] == "Linux":
        LINUX = True
    else:
        print("System Unknown")





'''Turns command switches on'''
def switchOn(arguments):
    global VERBOSE, NUKE

    for i in range(1, len(arguments)):
        if arguments[i] in commands:
            if str(arguments[i]) == "-v":
                VERBOSE = True
            elif str(arguments[i]) in commands == "--nuke":
                NUKE = True
            elif str(arguments[i]) in commands == "--show-bin":
                showBin()
            elif str(arguments[i]) == "-h" or str(arguments[i]) == "--help":
                usage()





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




'''Some commands can only be run if they are Specified Alone!'''
def sanity(arguments):
    if len(arguments) == 2:
        return True
    else:
        return False




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
    sys.exit()





'''Nuke the Trash Bin'''
def nuke():
    if MAC:
        os.system("rm -rf " + os.environ["HOME"] + "/.Trash/*")
    elif LINUX:
        os.system("rm -rf " + os.environ["HOME"] + "/.usr/local/files/*")
        os.system("rm -rf " + os.environ["HOME"] + "/.usr/local/info/*")

    print("Trash Bin Emptied")
    sys.exit()





def main():

    systemCheck()
    switchOn(sys.argv)

    '''Displays help menu'''
    if len(sys.argv) < 2:
        usage()

    '''Checks for too many arguments when nuke or show-nin'''
    if len(sys.argv) >= 3:
        if NUKE:
            print("!!! Nuke must be run alone !!!")
    else:
        if NUKE:
            nuke()
        else:
            multi_line(sys.argv)



main()
sys.exit()




