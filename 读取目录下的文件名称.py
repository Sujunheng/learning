# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 15:34:48 2018

@author: Junheng Su
"""
import os

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
 
list = GetFileList('D://WORK//IMAGES_ALL//1382销售//', [])
print(list)
count=0

f = open("D:/WORK/销售1.txt",'a')
for e in list:
        e=str(e)
        e=e.split('/')
        print(e[8])
        h='http://inno-pd-photo-store.oss-cn-hangzhou.aliyuncs.com/1382/'
        url=h+e[8]
        print(url)
        count+=1
        #e=e.decode(encoding='utf-8')
        #打开一个文件，准备以二进制写入文件
        f.write(url+'\n')#write并不是直接将数据写入文件，而是先写入内存中特定的缓冲区
        print(count)
f.close();#关闭文件

