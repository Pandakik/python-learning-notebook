# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 18:31:46 2020

@author: daxiguammm
"""

#Your codes need the ability to take different
#-action based on different conditions
print('example_1 example_1 example_1 example_1')
price = input('How much did you pay?')
price=float(price)
if price>=1.00:
    tax = .07#前面空四格，tab
    print('Tax rate is:'+str(tax))  #'>':greater than;'>='greater than or equal to
else:
    tax = 0
    print('Tax rate is:'+str(tax))
#表示方式二，因为不同的缩进，执行情况不相同
if price>=1.0:
    tax=.07
else:
    tax = 0
print('Tax rate is:'+str(tax))
print('\n')

#Be careful when comparing strings    
print('example_2 example_2 example_2 example_2')
country = 'CANADA'
if country=='canada':
    print('oh look a Canada')#String comparisons are case sensitive
else:
    print('You are not from Canada')
print('\n')

#Use functions to make case insensitive comparisons
print('example_3 example_3 example_3 example_3 ')
if country.lower() == 'canada'    :
    print('oh look a Canada')
else:
    print('You are not a Canada')
print('\n')    