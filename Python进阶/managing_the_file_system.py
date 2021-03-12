#Managing files

'''
-All the common operations are built into Python
Static or classless
os.path
    Old style
Class based
Path from pathlib library
    python 3.6 or higher
    Better performance as it can avoid calls to the OS    
'''
#demo1
#Working with paths

#Python 3.6 or higher
#Grad the library
from pathlib import Path

#Where am I?
cwd = Path.cwd()
print(cwd)

#Combine parts tp create full path and file name
new_file = Path.joinpath(cwd,'new_file.txt')
print(new_file)

#Does this exist?
print(new_file.exists())

#demo2

from pathlib import Path
cwd = Path.cwd()

#Get = cwd.parent

#Is this a directory?
print(parent.is_file())

#List child directories
for child in parent.iterdir():
    if child.is_dir():
        print(child)

#demo3
# Working with files
from pathlib import Path
cwd = Path.cwd()
demo_file = Path(Path.joinpath(cwd, 'demo.txt'))

#Get the file name
print(demo_file.suffix)

#Get the folder
print(demo_file.parent.name)

#Get the size
print(demo_file.stat().st_size)

'''
在载入前去检查文件大小，对发现事情有帮助，
做日志记录来解释为何工作和失败
'''