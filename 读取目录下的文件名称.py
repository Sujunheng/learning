# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 15:34:48 2018

@author: Junheng Su
"""
import os
import re

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
 
list = GetFileList('D:/WORK/第十五周/data_hudamodel/', [])
print(list)
count=0

f = open("D:/WORK/第十五周/hudamodeltext.txt",'a')
for e in list:
        e=str(e)
        e=os.path.split(e)
        print(e[1])
        ee=re.split(r"[_.]", e[1]) #多个分隔符
        eee=ee[0]+'_'+ee[1]+'-'+ee[2]+'-qroi'
        #h='http://inno-pd-photo-store.oss-cn-hangzhou.aliyuncs.com/1382/'
        #url=e[8]
        #print(url)
        count+=1
        #e=e.decode(encoding='utf-8')
        #打开一个文件，准备以二进制写入文件
        #f.write(e[4]+'\n')#write并不是直接将数据写入文件，而是先写入内存中特定的缓冲区
        print(count)
        #path="D:/WORK/第十五周/hudamodeltext/"+eee+"-roi"+".txt"
        #if  not os.path.exists(path):       #判断目录是否存在，否则创建
                       # os.makedirs(path)
        froi = open("D:/WORK/第十五周/hudamodeltext/hudaqroi/"+eee+".txt",'w')
        froi.write('[{"x":"0.0036","y":"0.0006"},{"x":"0.0011","y":"0.0280"},{"x":"0.0253","y":"0.0030"},{"x":"0.0036","y":"0.0030"}]')
        froi.close();
f.close();#关闭文件