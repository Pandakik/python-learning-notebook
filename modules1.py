# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:19:01 2020

@author: daxiguammm
"""

#Modules
#What's the modules?
#A python file with functions ,classes and other components
#Why use the modules?
#Break code doun into reusable structures

#Import a mudule

#fucntion 1
#import module as namespace
import helpers
helpers.display('Not a worning')

#function 2
#import all into current namespace
from helpers import *
display('Not a worning')

#function 3
#import specific items into current namespace
from helpers import display
display('Not a worning')