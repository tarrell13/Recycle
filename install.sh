#!/bin/bash

# This script will run the necessary commands to install the proper python interpreter and modules
#Authur: Tarrell Fletcher
#Date: December 16, 2016
#Last Modified: December 18, 2016
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


if [ $(uname) == "Darwin" ]; then

    # (1) Install homebrew
    # (2) Install Python3
    # (3) Install send2trash module

    if [ $(which brew) == ]; then
        /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    fi

    if [ $(which python3) == ]; then
        brew install python3
        sudo pip3 install send2trash
    fi

sudo cp recycle.py /usr/local/bin/recycle

elif [ $(uname) == "Linux" ]; then

    #YUM based Installation
    if [ $(ls /etc | grep yum.conf) == "yum.conf" ]; then

    # (1) Installing Python3 from Source
    # (2) Installs send2trash module

        if [ $(which python3) == ]; then
            sudo yum install yum-utils -y
            sudo yum-builddep python -y
            curl -O https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tgz
            tar xf Python-3.5.0.tgz
            cd Python-3.5.0
            ./configure
            make
            sudo make install
            pip3 install send2trash
            cp recycle.py /usr/local/bin/recycle
        fi

    #DEBIAN based Installation
    elif [ $(ls /etc | grep apt) == "apt" ]; then

        # (1) Install Python3
        # (2) Install send2trash

        if [ $(which python3) == ]; then
            sudo apt-get install python3 -y
        fi

        if [ $(which pip3) == ]; then
            sudo apt-get install python3-pip -y
            sudo pip3 install send2trash
        fi

        sudo cp recycle.py /usr/local/bin/recycle
    fi
fi


#Changes interpreter if not in default location
if [ $(which python3) != "/usr/local/bin/python3" ]; then
        sed -i "s/\/usr\/local\/bin\/python3/\/usr\/bin\/python3/g" recycle.py
fi

#Adding the command to the PATH
