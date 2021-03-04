# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 19:07:42 2020

@author: daxiguammm
"""

#LOOPS
#For
#Loop through a collection
for name in ['Mike','Sussan']:
    print(name)
print('\n')    
#What range will do for you is it will automatically create a list of numbers for you
for index in range(0,2):#[0,1]
    #第一个数字是起始数字，第二个数字是结束数字，但不包括第二个数字（整数）
    print(index)

#while    
#Loops with a condition
names = ['Meiko','Susan']    
index = 0
while index < len(names):
    print(names[index])
    index = index + 1