#文件备份
def copyFile():
    #接收用户输入的文件名
    old_file=input('请输入要备份的文件名： ')
    file_list=old_file.split('.')
    #新文件的名字
    newfile=file_list[0]+'_备份.'+file_list[1]
    with open(old_file,'r',encoding='utf-8') as f1,open(newfile,'w',encoding='utf-8') as f2:
        for line in f1:
            f2.write(line)
    pass
copyFile()