#文件的操作
#打开文件关键字 open
#默认编码是GBK（中文编码)，最好在每次操作文件时指定编码为utf-8
# fobj=open('test1.txt','w',encoding='utf-8')
# fobj.write('这是第一行内容-测试\r')
# fobj.write('这是第二行内容-测试\r')
# fobj.write('这是第三行内容-测试\r')
# fobj.close()
# fobj=open('test1.txt','ab')
# fobj.write('这是第一行内容-测试\r'.encode('utf-8'))
# fobj.write('这是第二行内容-测试\r'.encode('utf-8'))
# fobj.write('这是第三行内容-测试\r'.encode('utf-8'))
# fobj.close()
# fobj=open('test1.txt','r',encoding='utf-8')
# # for i in fobj:
# #     print(i)
# print(fobj.readline())
# print(fobj.readline())
# print(fobj.readline())
# fobj.close()    #文件对象关闭掉，否则会造成文件泄露或者文件锁
# print(fobj.readline().decode('utf-8'))
# print(fobj.readline().decode('utf-8'))
# print(fobj.readline().decode('utf-8'))

#with 上下文管理
#with语句，不管在处理文件过程中是否发生异常，都能保证with语句执行完毕后已经关闭打开的文件句柄。
# with open('test1.txt','a',encoding='utf-8') as f:
#     #print(f.read())
#     f.write('这是以withopen模式打开的')