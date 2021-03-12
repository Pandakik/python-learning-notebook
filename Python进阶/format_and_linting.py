    # -*- coding: utf-8 -*-
    """
    Created on Thu Oct  8 16:48:41 2020
    
    @author: daxiguammm
    """
    
    #This is valid Pythin code
    #But,it's not really readable code
    x = 12
    if x==24:
        print('Is valid')
    else:
        print('Not valid')    
        
    def helper(name='sample'):
        pass
    
    def another(name="sample"):
        pass    
    
    #Formatting matters
    '''
    Make code readable
    Easier to debug
    Consistency helps everyone
    '''    
    #PEP 8
    '''
    Python Enhancement Proposal#8
    All about formatting
    '''
    
    #Common rules
    '''
    Spaces,not tabs
    variable_name,not variableName or VariableName
    Avoid extraneous whitespace (避免无关的空格)
    {'good':42}
    {'bad' : 20}
    '''
    
    #Linting
    #is going to be there to help support you -
    #-when it comes to all these different types of issues
    '''
    -Identify formatting issues
    Common for all languages
    
    -Pylint for Python
    # Windows
    pip install pylint
    # macOS or Linux
    pip3 install ptlint
    
    -Configurable to ignore certain rules
    Avoid doing this
    
    -Automatically run ny Visual Studio Code
    '''
    
    #Use docstring for inlune documentation
    def print_hello(name: str) -> str:
        '''
        Greets the user by name
        
        Parameters:
            name(str):The name of the user
        Returns:
            str: The greeting
        '''
        print('Hello, ' + name)
    
    
    #The challenge with weakly tyoed languages
    def get_greeting(name)
        return 'Hello, '+name
    
    message = get_greeting(42)#会出错，因为格式问题
    print(message)    
    
    
    #Type hints
    '''
    Tell the editor and linter what data types to expect
    DOES NOT cause "compiler" error
    '''
    
    def get_greeting(name:str) -> str:
        return 'Hello, ' + name 
