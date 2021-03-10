# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 19:00:27 2020

@author: daxiguammm
"""

#Classes define data structures and behavior
'''
-Why use classes
Create reusable components
Group data and operations together

Moving parts
Classes are nouns
Properties are adjectives
Methods are verbs
'''
#Creating a class
#命名格式：PascalCasing
class Presenter():
    def _init_(self,name):#第一个参数是self
        #Constructor
        self.name = name#Filed，属性
    def say_hello(self):
        #method
        print('Hello, '+self.name)
        
#Using a class
presenter = Presenter('Chris')
presenter.name='Christopher'
presenter.say_hello()

#Accessiblity in Python
'''
EVERYTHING is public
Conventions for suggesting accessiblility
_means avoid unless you really know what you're doing
__(double underscore) means not use

'''

#Adding properties
#设置属性
class Presenter():
    def __init__(self,name):#第一个参数是self
        #Constructor
        self.name = name#Filed，属性
    @property     #设置属性
    def name(self):
        print('In the getter')
        return self.__name
    @name.setter
    def name(self,value):
        print('In hte setter')
        #cool validation here
        self.__name = value

#Using a property
presenter = Presenter('Chris')
presenter.name='Christopher'
print(presenter.name)






