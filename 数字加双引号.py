# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 17:56:19 2018

@author: Su.Jun
"""
import csv
import json
#数字转换
'''
def dic_change(dic):
    couont=len(dic)
    fs=open('D:/WORK/第十一周/fishdata_new/data_Modelaccuracytest/2231/data/新建文本文档.txt',"wb"):
    for i in range (count):
        dic[i]["x"]='\"'+str(dic[0]['x'])+'\"'
        dic[y]["x"]='\"'+str(dic[0]['x'])+'\"'
    f.close()
'''
csv_reader = csv.reader(open('D:/WORK/第十四周/转换坐标点.csv', encoding='utf-8'))
dic=[]
i=0
for i in csv_reader:
    dic.append(i)
    #print(i)
count=len(dic)
target_list = [int(x) for x in dic[0][0].split('')]

