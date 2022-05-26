#import time #导入模块
#print(time.ctime())


# from time import ctime,time
# print(ctime())

import time as mytime  #取别名
'''OS模块'''
import os
#重命名文件
#os.rename('test12.txt','testoa.txt')
#删除文件
#os.remove('testoa.txt')
#创建文件夹
#os.mkdir('tttt')
#删除目录，目录必须为空
#os.rmdir('tttt')
#删除多级目录，目录必须为空
'''如果要删除非空目录，需要使用shutil模块的rmtree（）'''
'''import shutil
shutil.rmtree('F:/test/')   #直接删除非空目录'''
#os.removedirs('ttttt')
#mkdir 只能创建一级目录，当上一级目录不存在时报错。
#os.mkdir('F:/test/subtest')
#makedirs()可以创建多级目录，当上一级目录不存在时也可以创建。
#os.makedirs('F:/test/subtest')
#获取当前的目录
#print(os.getcwd())
#路径的拼接
# print(os.path)
# print(os.path.join(os.getcwd(),'venv'))
#获取目录列表
#print(os.listdir('F:/'))   #经典方式
#现代版方法 scandir 和 with 一起来使用，上下文管理器（with）会在迭代器遍历完成后自动释放资源
# with os.scandir('F:/') as entries:
#     for entry in entries:
#         print(entry.name)
#遍历路径，并判断是否为文件
# basepath='F:/'
# for entry in os.listdir(basepath):
#     #if os.path.isfile(os.path.join(basepath,entry)):
#     if os.path.isdir(os.path.join(basepath,entry)):
#         print(entry)
#递归遍历所有级别目录
# def scan(path):
#     for entry in os.listdir(path):
#         if os.path.isfile(os.path.join(path,entry)):
#             print(entry)
#         elif os.path.isdir(os.path.join(path,entry)):
#             scan(os.path.join(path,entry))
# print(scan('F:/Test'))