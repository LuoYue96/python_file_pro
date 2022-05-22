#文件的操作
#打开文件关键字 open
#默认编码是GBK（中文编码)，最好在每次操作文件时指定编码为utf-8
# fobj=open('test1.txt','w',encoding='utf-8')
# fobj.write('这是第一行内容-测试\r')
# fobj.write('这是第二行内容-测试\r')
# fobj.write('这是第三行内容-测试\r')
# fobj.close()
fobj=open('test1.txt','ab')
fobj.write('这是第一行内容-测试\r'.encode('utf-8'))
fobj.write('这是第二行内容-测试\r'.encode('utf-8'))
fobj.write('这是第三行内容-测试\r'.encode('utf-8'))
fobj.close()