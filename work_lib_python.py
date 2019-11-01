# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 10:11:53 2019

@author: 蘇
"""
import os
import re
import numpy as np

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
 
fileList = GetFileList(r'C:\work_project\brandmax\fca_test\fca_logs', [])

file_dic = {}
with open(r'C:\work_project\brandmax\fca_test\mac_count.txt','w') as f_write:
    for i in fileList:
        with open(i,'r',encoding='gbk') as f_read:
            mac_info = f_read.readlines()
            int_mac_count = list(map(int,mac_info))
            file_dic[i] = int_mac_count
            print(len(int_mac_count))
            print(np.sum(int_mac_count))
            datetime = re.split(r'[_.]',str(os.path.basename(i)))[1]
            str_i = datetime
            list_i = list(str_i)    # str -> list
            list_i.insert(4, '/')   # 注意不用重新赋值
            list_i.insert(7, '/')          
            str_datetime = ''.join(list_i)    # list -> str
            print(str_datetime)
            f_write.write(str_datetime+' '+str(len(int_mac_count))+' '+str(np.sum(int_mac_count))+'\n')

        