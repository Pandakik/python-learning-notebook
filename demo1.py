#Adding properties
#设置属性
class Presenter():
    def __init__(self,name):#第一个参数是self
        #Constructor
        self.name = name#Filed，属性
    @property     #设置属性
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        #cool validation here
        self.__name = value
    def say_hello(self):
        print('Hello '+self.name)
#Using a property
presenter = Presenter('Chris')
presenter.name='Christopher'
print(presenter.name)
presenter.say_hello()
