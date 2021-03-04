# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:38:46 2020

@author: daxiguammm
"""

#Virtual environments
#By default,package are installed globally
#version management becaomes a challenge
#Virtual environment can be used to contain and manage package collections
#Relly just a folder behind the scenes with your  all your packages

#Creating virtual environments
#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#Instal virtual environment
pip instal virualenv

#Windous system
python -m venv <folder name>

#osx/Linux(bash)
virtualenv <folder name>
#↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

#Using virtual environment
#cmd.exe
<folder_name>\Scripts\Activate.bat
#Powershe11
<folder_name>\Scripts\Activate.ps1
#bash she11
../<folder_name>/Scripts/activate

    #osx/Linux (bash)
<folder_name>/bin/activate