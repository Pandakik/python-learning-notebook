#使用with来进行清理操作
#Writing to a file
stream = open('output.txt', 'wt')
stream.write('Lorem ipsum dolar')
stream.close()#This is really important!!

#Re - writing with a try/finally
try:
    stream = open('output.txt', 'wt')
    stream.write('Lorem ipsum dolar')
finally:
    stream.close()#THIS IS REALY IMPORTANT!!!
#with
with open('output.txt', 'wt') as stream
    stream.write('Lorem ispsum dolar')      
#with能保证文件在执行完成后关闭文件
#不管运行时是否发生报错    