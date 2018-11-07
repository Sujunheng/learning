# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 14:23:32 2018

@author: Junheng Su
"""
import os
#获取文件目录
def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir.encode('utf-8'))
    elif os.path.isdir(dir):  
        for s in os.listdir(dir):
            #如果需要忽略某些文件夹，使用以下代码
            #if s == "xxx":
                #continue
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)  
    return fileList

#读取文件目录下的文件名，并写入
for i in range(4):
    a=20180827
    b=i+a
    b=str(b)
    list = GetFileList('D://WORK//'+b+'//重复顾客//', [])
    count=0
    f = open("D:/WORK/TXT/"+b+"重复顾客.txt",'a+')
    for e in list:
        print(e)
        count+=1
        print(count)
        e=e.decode(encoding='utf-8')
        #打开一个文件，准备以二进制写入文件
        f.write(e+'\n')#write并不是直接将数据写入文件，而是先写入内存中特定的缓冲区
        print(count)
    f.close();#关闭文件
f.close();


#合并txt文件
filedir ='D://WORK//TXT'
#获取当前文件夹中的文件名称列表  
filenames=os.listdir(filedir)
#打开当前目录下的result.txt文件，如果没有则创建
f=open('D://WORK//TXT//result.txt','w')
#先遍历文件名
for filename in filenames:
    filepath = filedir+'/'+filename
    #遍历单个文件，读取行数
    for line in open(filepath):
        f.writelines(line)
    f.write('\n')
#关闭文件
f.close()