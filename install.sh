#!/bin/bash

# This script will run the necessary commands to install the proper python interpreter and modules
#Arthur: Tarrell Fletcher
#Date: December 16, 2016
#Last Modified: N/A
#Email: Tarrell13@verizon.net
#
#Program will place items in the recycle bin instead of deleting them
#Usage: ./recycle OPTIONS <File or Directory>
#Options:
#-v:     Verbose Output
#
#Example: (1) ./recycle boo.txt 
#---------(2) ./recycle boo.txt foo.txt
#---------(3) ./recycle dir
#---------(4) ./recycle *.txt


#To run this script open command terminal and type "./Install.sh" 
#After running this script you should be able to run the ./recycle script
#Will add the command to the PATH so user can just simply type "recycle" to run the program 


#Install homebrew 
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

#Install Python3
brew install python3

#Install send2trash
sudo pip3 install send2trash


#Adding the command to the PATH
cp recycle.py /usr/local/bin/recycle

