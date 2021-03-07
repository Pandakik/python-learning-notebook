# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 18:30:34 2020

@author: daxiguammm
"""

#To get current date and time
#We need to use the datetime library

from datetime import datetime#这是个时间的库函数

print('This is example1')
current_date = datetime.now()#得到现在的时间
#The now function returns a datetime object
print('Today is:'+str(current_date))


print('This is example2')
from datetime import datetime,timedelta#这是个时间的库函数
today = datetime.now()
print('Today is:'+str(today))

#timedelta is used to define a period of time
one_day = timedelta(days=1)
yesterday = today-one_day
print('Yesterday was:'+str(yesterday))
