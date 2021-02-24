# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:55:51 2020

@author: daxiguammm
"""
from pip._vendor.colorama import init,Fore
def display(message,is_warning=False):
    if is_warning:
        print(Fore.GREEN+message)
    else:    
        print(Fore.BLUE+message)    