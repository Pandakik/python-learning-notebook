# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 20:14:51 2020

@author: daxiguammm
"""

#We already learned to create functions which accept a parameter and return values

#Example1
def get_initial(name,force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input('Enter your first name:')
first_name_initial = get_initial(first_name,False)

print('Your initial is:' + first_name_initial)

#Example2
def get_initial(name,force_uppercase=True):#第二个位置有默认值，就不同输入了
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1].upper()
    return initial

first_name = input('Enter your first name:')
first_name_initial = get_initial(first_name)

print('Your initial is:' + first_name_initial)

#You can also assign the values to parameters
#by name when you call the function


#Example3
first_name_initial = get_initial(force_uppercase=False,name=first_name)#指定参数，可以不用顺序传
