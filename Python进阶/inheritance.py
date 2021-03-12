#Inheritance 继承
#What is inheritance?
'''
It's a genneralization spaceilaization
是一般化-特殊化
SQL和MYSQL都是数据连接类型
“has a”是通过属性处理
“is a”关系是继承
'''
#Create an 'is a' relationship
'''
Student is a person
SqlConnection is a DatabaseConnection
MySalConnection is a DatabaseConnection
'''
#Compositon(with properies)creates a 'has a'relationship
'''
Student has a Class
DatabaseConnection has a ConnectionString
'''

#Pythin inheritance in action
'''
-All method are 'virtual'
Can override or redefine their behavior
-Keyword super to access parent class
Constructor
Properties in methods
-Must always call parent constructor
'''

#Demo
#Inheriting from a class
class Person():
    def __init__(self,name):
        self.name = name
    def say_hello(self):
        print('Hello, '+self.name)

#Student继承Person
class Student(Person):#在括号里写父辈的类名字
    def __init__(self, name, school):#指明参数，name来自于person
       #我们调用父级构造函数来设置name
        super().__init__(name)#当从类派生时，要调用父级构造函数
        self.school = school
    def sing_school_song(self):
        print('Ode to ' + self.school)          

#Using a derived class
student = Student('mike','HDU')
student.say_hello()
student.sing_school_song()
#what are you?
#继承时创建的“is a”的关系
print(isinstance(student,Student))#student是Studen吗？
print(isinstance(student,Person))#student是Person吗？
print(issubclass(Student,Person))

print(f'Is this a student? {isinstance(student,Student)}')
print(f'Is this a Person? {isinstance(student,Person)}')
print(f'Is this a Person? {issubclass(Student,Person)}')
'''
在py中创建一个类，自动继承自Object，是Py中的基础
我们也总可以重写函数，包括根对象上的
也可以添加功能
'''

#修改
class Student(Person):#在括号里写父辈的类名字
    def __init__(self, name, school):#指明参数，name来自于person
       #我们调用父级构造函数来设置name
        super().__init__(name)#当从类派生时，要调用父级构造函数
        self.school = school
    def sing_school_song(self):
        print('Ode to ' + self.school)      
    def say_hello(self):
        #Let the parent do some work
        super().say_hello()
        #Add on custom code
        print('I am very happy!')   


#__str__功能：自动转换为字符串
class Student(Person):#在括号里写父辈的类名字
    def __init__(self, name, school):#指明参数，name来自于person
       #我们调用父级构造函数来设置name
        super().__init__(name)#当从类派生时，要调用父级构造函数
        self.school = school
    def sing_school_song(self):
        print('Ode to ' + self.school)      
    def say_hello(self):
        #Let the parent do some work
        super().say_hello()
        #Add on custom code
        print('I am very happy!')   
    def __str__(self):
        return f'{self.name} attedns {self.school}'

student = Student('mike','HDU')
print(syudent)#没有str函数的话，会返回一串代码