#!/bin/bash

# Based upon setup script used in Budget-Analyzer

### Install Python3.9
### Initialize Virtual Environment
### Install dependencies
### Activate venv

### view system information
uname -a
bash --version

echo;echo;echo

###
### TO BE DONE: check if script has already been run
###             or if requirements have already been fulfilled
###

### Check if Homebrew is Installed
brew --version 2>/dev/null
if [ $? -eq 0 ]
then
    brew_installed=1
    echo "HomeBrew Installed"
else
    echo "Homebrew NOT installed"
    brew_installed=0
fi



###
### KICKOFF INSTALLS
###
install_homebrew() {
    echo "NOTE: YOU WILL BE PROMPTED FOR SUDO PASSWORD BY HOMEBREW"
    read -n 1 -p "Do you wish to continue? (Y/n) " docontinue; echo ""

    awk -vs1='y' -vs2=${docontinue} 'BEGIN {
        if ( tolower(s1) == tolower(s2) ){
            exit 0 # continue
        } else {
            exit 2 # do not continue
        }
    }'

    if [ $? == 0 ]
    then
        echo "Onwards..."; sleep 2
        command -v brew >/dev/null 2>/dev/null
    else
        echo "Quitting"
        exit 2
    fi
}

if [ $brew_installed -eq 0 ]
then
    echo "INSTALL HOMBEBREW PLACEHOLDER"
else
    echo "DO NOT INSTALL..."
fi

install_homebrew