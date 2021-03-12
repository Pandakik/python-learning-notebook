"""
Created on Sun Oct 11 16:06:53 2020

@author: daxiguammm
"""
#多重继承
#Mixins(multiple inheritance)
#一句话：We're not launching rockets here

#inherit from multiple classes
#A little controversial
'''
Can get messy quickly
Manny modern languages only support single inheritance
'''
#Uses
'''
Enable functionality for fameworks such as Django
Streamline repetitious operations
'''

#The scenario 
'''
-What I want to create
Helper database class
Create different types for different databases
-What I want it to be able to do
Connect to a database
Log what it's doing
'''
#Supporting classes
class  Loggable:
    def __init__(sself):
        self.title = ''
    def log(self):
        print('Log message from ' + self.title)

class Connection:
    def __init__(self):
        self.server = ''
    def connect(self):
        print('Connection to database on' + self.server)                

#Create out "framework"

def framework(item):
    #Perform the connection
    if isinstance(item, Connection):
        item.connect()
    #Log the operation
    if isinstance(item, Loggable)
        item.log()


            
#Create our database class
class SqlDatabase(Connection, Loggable):
    def __init__(self):
        super().__init__()
        self.title = 'SQL Connection Demo'
        self.server = 'Some_Server'                

#Putting it to work
# #Create an instance of our class
sql_connection = SqlDatabase()
# Use our framwork        
framework(sql_connection)#connects and logs