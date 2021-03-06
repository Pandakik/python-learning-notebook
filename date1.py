# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 18:30:34 2020

@author: daxiguammm
"""

#To get current date and time
#We need to use the datetime library

from datetime import datetime#这是个时间的库函数

print('This is example_1')
current_date = datetime.now()#得到现在的时间
#The now function returns a datetime object
print('Today is:'+str(current_date))


print('This is example_2.1')
from datetime import datetime,timedelta#这是个时间的库函数
today = datetime.now()
print('Today is:'+str(today))
#timedelta is used to define a period of time
one_day = timedelta(days=1)
yesterday = today-one_day
print('Yesterday was:'+str(yesterday))
print('This is example_2.2')
one_week = timedelta(weeks = 1)
last_week = today-one_week
print('Last week is:'+str(last_week))


print('This is example_3')
from datetime import datetime
current_time = datetime.now()
print('Day is: '+str(current_date.day))
print('Month is: '+str(current_date.month))
print('Year is:  '+str(current_date.year))

print('This is example_4')
#I say my birthday is the fifth of june 1999.
#Sometime you receive the date as a string and need to convert it to datetime object
from datetime import datetime
birthday = input('When is your birthday (dd/mm/yyyy)?')
birthday_date = datetime.strptime(birthday,'%d/%m/%Y')
print('Birthday: '+str(birthday_date))














