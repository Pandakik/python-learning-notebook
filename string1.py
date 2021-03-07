# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:01:30 2020

@author: daxiguammm
"""
#example 1
#创建变量时用这样的形式：word_word
first_name ='Christopher'
last_name = 'harrison'
print(first_name + last_name)
print('hello '+first_name+' '+last_name)

#excample 2
#you can use functions to modify strings
sentence = 'The dog is named Sammy'#define a string
print(sentence.upper())#convert everything into uppercase letters
print(sentence.lower())#convert everything into lowercase letters
print(sentence.capitalize())#capitalize just the first word
print(sentence.count('m'))#potentially count all of the instance of a particular string

#example 3
#The function help us to format strings we save to files and databases,or display to users.
first_name = input('What is your first name?')
last_name = input('What is your last name?')
print('hello '+first_name.capitalize()+' '+last_name.capitalize())
#demo;demonstration means demonstration case;示范;

#Just hit tap and that will complete it out for you

#example4 
#实例4 格式化字符串
output = 'hello, '+first_name+''+last_name
print(output)
output = 'hello,{},{}'.format(first_name,last_name)
print(output)
output='hello,{0}{1}'.format(first_name,last_name)
print(output)
#Only available in Python 3
output = f'Hello,{first_name}{last_name}'
print(output)