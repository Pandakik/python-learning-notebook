# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 19:22:24 2020

@author: daxiguammm
"""

#Functions make your code more readable and easier to maintain
#Always add comments to explain the purpose of your functions
#Functions must be declared  before the line of code where the function is called

#Examole_!
import datetime

#Print the current time
def print_time():
    print('take completed')
    print(datetime.datetime.now())
    print()
    
first_name = 'Susan'    
print_time()

for x in range(0,10):
    print(x)
print_time() 

#Exmaple_2   
from datetime import datetime#改进版
def print_time2():
    print('take completed')
    print(datetime.now())
    print()
    
    
#Example3
from datetime import datetime#改进版

def print_time0(task_name):
    print(task_name)
    print(datetime.now())
    print()

first_name = 'Susan'    
print_time0('printed first name')

for x in range(0,10):
    print(x)
print_time0('completed for loop')    


#Example4
#Ask for someones name and return the initials
first_name = input('Enter your first name:')
first_name_initial = first_name[0:1]

middle_name = input('Enter your middle name:')
middle_name_initial = middle_name[0:1]

last_name = input('Enter your last name:')
last_name_initial = last_name[0:1]

print('Your initials are:'+first_name_initial+middle_name_initial+last_name_initial)

#Example5
#Ask for someones name and return the initials

def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('Enter your first name:')
first_name_initial = get_initial(first_name)

middle_name = input('Enter your middle name:')
middle_name_initial =get_initial(middle_name)

last_name = input('Enter your last name:')
last_name_initial =get_initial(last_name)

print('Your initials are:'+first_name_initial+middle_name_initial+last_name_initial)










    