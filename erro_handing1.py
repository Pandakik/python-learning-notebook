# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 19:08:33 2020

@author: daxiguammm
"""

#Stntax erros语法错误
print('This is example_1')
x = 42
y = 42
#if x==y: #right
#if x==y #error
print('Success!!')
    
#Runtime errors运行错误
#This code will fail when run
print('This is example_2')
x = 42
y = 0
#print(x/y) #error

#Catching runtime errors
try:
    print(x/y)
except ZeroDivisionError as e:
    print('Sorry,something went wrong!')
except:
    print('Something really went wrong!')
finally:
    print('This always runs on success or farlure')
        


#Logic errors
#This code won't run at all
    print('This is example_3')
x = 206
y = 42
if x<y:
    print(str(x)+'is greater than'+str(y))#error前面的运算符是小于，这里又说‘greater’,逻辑错误
    