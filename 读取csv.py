# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 11:37:09 2018

@author: Su.Jun
"""
import pandas as pd
import numpy as np

#open csv with pandas
def open_csv():
    global df
    with open ('D:/WORK/第十六周/不同灯光.csv','r') as f:
    
        df=pd.read_csv(f,header=None,sep=',') 
    #filename可以直接从盘符开始，标明每一级的文件夹直到csv文件，header=None表示头部为空，
    #sep=' '表示数据间使用空格作为分隔符，如果分隔符是逗号，只需换成 ‘，’即可。
    return df

#循环建立文档，并保存相应信息
    #data文件夹 人工打点 文件名称 stationid_id_logtime
'''  
id	station_id	pic	fish_id	logtime
22943	1979	ht	             2018/10/2 10:50
22940	1979	h	             2018/10/2 11:05
22939	1979	h1	             2018/10/2 11:10
'''

#data 存放人工打点数据
#huda_data 存放湖大模型坐标数据
#roi 存放ROI数据
def creat_savefile():
    #len(df[0])=100
    for i in range (1,48):
        ymdhm=df[4][2].replace('/','-')
        ymd=ymdhm.split(' ')
        #data
        #path='D:/WORK/第十五周/data_大样本测试/不同灯光/man/data/'+df[1][i]+'_'+df[0][i]+'-'+ymd[0]+'.txt'
        #roi
        path='D:/WORK/第十五周/data_大样本测试/不同灯光/huda/roi/'+df[1][i]+'_'+df[0][i]+'-'+ymd[0]+'-roi'+'.txt'
        with open(path,'w') as dataf:
            # 人工打点 dataf.write('{"customer":'+df[10][i]+'}')
            # 机器打点 dataf.write(df[5][i])
            #roi
            dataf.write(df[13][i])


if __name__ == '__main__':
    open_csv()
    creat_savefile()

    