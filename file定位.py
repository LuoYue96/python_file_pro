#tell 返回文件指针当前所在的位置
#对于中文来讲，每次读取到的一个汉字在gbk中占用两个字符，在utf-8中占用三个字符，英文字母统一占用1个字符
# with open('test1_备份.txt','r',encoding='utf-8') as f:
#     print(f.read(3))
#     print(f.tell())
#     print(f.read(2))
#     print(f.tell())

#truncate 可以对源文件进行截取操作
# with open('./test1_备份.txt','r+',encoding='utf-8') as f1:
#     print('截取之前内容：')
#     print(f1.read())
#     print('截取之后内容：')
#     f1.truncate(2)  #只保留前5个字符
#     print(f1.tell()) #tell不随truncate改变，依然停留在f1上一次读完时的光标位置
#     print(f1.read())

#seek  如果在操作文件的过程，需要定位到其他位置进行操作，用seek()；seek(offset,from)有2个参数，offset 偏移量单位字节，负数
#是往回偏移，正数是往前偏移，from位置：0表示文件开头，1表示当前位置，2表示文件末尾
# with open('test1.txt','rb') as f:
#     data = f.read(3)
#     print(data.decode('utf-8'))
#     f.seek(-3,1) #光标从当前位置向左移动3个字符，相当于光标又设置到了0的位置
#     print(f.read(3).decode('utf-8'))
#     f.seek(-9,2)    #光标定位到 从末尾开始向左数第9个字符
#     print(f.read().decode('utf-8'))
#     print(f.tell())
#     f.seek(3,0)     #光标定位从文章开头向后移动9个字符
#     print(f.tell())
#     print(f.read().decode('utf-8'))
#当使用 r 模式打开文件，只允许从文件的开头计算相对位置，如果从文件尾部或者当前位置计算的话，
# 就会引发异常io.UnsupportedOperation:can't do nonzero cur-relative seeks.用rb可以自由调整位置
