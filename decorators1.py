# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:55:12 2020

@author: daxiguammm
"""

#PRogramming components
'''
Objiects
-Nouns
-Data constructs

Function/Methods
-Verbs
-Actions
'''

#Decorators
'''
Adjectives
Add additional functinality to code
Common in frameworks
Django
Flask
'''

#Using a decorator
'''
Snippet from Flask
register https://myserver/api/products
'''
@route('api/products')
def get_products:
    #code to list from database
    pass
    
#Creating a decorator
def logger(func):
    def wrapper():
        print('Logging execution')
        func()
        print('Done logging')
    return wrapper
        


    