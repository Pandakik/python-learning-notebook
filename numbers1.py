# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:53:58 2020

@author: daxiguammm
"""

#数字与字符串类型的转换
#Numbers can be sorted in variable
print('This is example_1')
pi = 3.14159625
print(pi)

#You can do math with numbers
print('This is example_2')
first_num = 6
second_num = 2
print(first_num+second_num)
print(first_num*second_num)
print(first_num**second_num)#“**”是指数运算

#If you cobine numbers with strings,Python ges confused
print('This is example_3')
days_in_feb=28
#print(days_in_feb+'days in February') #when we run this it blows up 
#Unsupported operand type for plus and string

print('This is example_4')
days_in_feb=28
print(str(days_in_feb)+'days in February')#sttr(),字符转换

print('This is example_5')
first_num='5'
second_num='6'
print(first_num+second_num)

print('This is example_6')
print(int(first_num)+int(second_num))
print(float(first_num)+float(second_num))

print('This is example_7')
first_num = input('Pleas enter a number：')
second_num=input('Please enter another number:')
print(first_num+second_num)#注意input返回的是字符串，不是数字；
print(int(first_num)+int(second_num))#注意input返回的是字符串，不是数字；




















