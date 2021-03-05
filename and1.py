# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:33:53 2020

@author: daxiguammm
"""

#Sometime you can combine conditions with AND instead of nesting if statements
gpa = float(input('What was your Grade Point Average?'))#注意输入值类型
lowest_grade=float(input('What was your lowest grade?'))#注意输入值类型
if gpa >= 0.85 and lowest_grade >= 0.7:
    print('Well done!')
print('\n')   
#use Boolean variables as flags
if gpa >= 0.85 and lowest_grade >= 0.7:
    honour_roll=True
else:
    honour_roll=False
#Somewhere in your code
if honour_roll:    
    print('Well done!')    