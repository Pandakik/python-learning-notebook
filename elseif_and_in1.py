# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:00:55 2020

@author: daxiguammm
"""
country=input('What country do you live in?')
province=input('What province do you live in?')
#If only one of the conditions will ever occur-
#-you can use a single if starement with elif
print('example_1 example_1 example_1 example_1')
if province=='Alberta':
    tax=0.05
elif province=='Nunavut':
    tax=0.05
elif province=='Ontario':
    tax=0.03
else:
    tax=0.15
print('Tax rate is:'+str(tax))    
print('\n')        
    
print('example_2 example_2 example_2 example_2')
#or的使用    
if province=='Alberta' or province=='Nunavut':
    tax=0.05

elif province=='Ontario':
    tax=0.03
else:
    tax=0.15
print('Tax rate is:'+str(tax))
print('\n')        
        
#If you have a list of possible values to check,
#you can use the IN operator
print('example_3 example_3 example_3 example_3')
if province in ('Alberta','Nunavut','Yukon'):
    tax =0.05
elif province=='Ontario':
    tax=0.03
else:
    tax=0.15    
print('Tax rate is:'+str(tax))
print('\n')  
     
#If an action depends on a combination of conditions
# you can nest if statement    
print('example_4 example_4 example_4 example_4')
if country.lower() == 'canada':
    if province in ('Alberta','Nunavut','Yukon'):
        tax =0.05
    elif province=='Ontario':
        tax=0.03
    else:
        tax=0.15    
    print('oh look a Canada')
else:
    tax=0
    print('You are not a Canada')
print('Tax rate is:'+str(tax))
print('\n')    