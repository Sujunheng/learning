# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 15:37:19 2018

@author: Junheng Su
"""
import urllib.request
#import webbrowser
#import codecs
#import time
import os
import re 
count = 0
errolist=[]
time='第十五周'
#man or roboot
kind='huda'
filepath='D:/WORK'
filename='hudamodeltext/'
#file=原始图片 还是机器识别图片
file='url'
#D:/WORK/第十二周/movecartext/1763_ooxx.txt
picture_url_path=filepath+'/{time}/{filename}/{file}.txt'.format(time=time,filename=filename,file=file)

with open(picture_url_path) as fp:
        for ebayno in fp:
            try:#异常检测
                each = ebayno.strip() #.split()
                url=each   #获取图片url
                #print(url)
        #time.sleep(0.5) #打开间隔时间
                #print(url)
        #webbrowser.open(url) #打开网页


                if(url.find('.') != -1):#2
                    r=url.split('/')  #url切割得到图片名称
                    rr=r[3].split('_')
                    rrr=rr[2]+"_"+rr[5]+rr[3]+"-"+rr[4]+'.png'
                    print(rrr)
                    bytes = urllib.request.urlopen(url);
                    ##D:/WORK/第十二周/movecartext/roboot/r[2]/
                    path=filepath+'/{time}/{filename}/{kind}/'.format(time=time,filename=filename,kind=kind)  #本地目录加店的代号，得到按店号存放的图片目录
                    if  not os.path.exists(path):       #判断目录是否存在，否则创建
                        os.makedirs(path)
                    f = open(path+rrr, 'wb');  #代开一个文件，准备以二进制写入文件
                    f.write(bytes.read());#write并不是直接将数据写入文件，而是先写入内存中特定的缓冲区
                    f.flush();#将缓冲区的数据立即写入缓冲区，并清空缓冲区
                    f.close();#关闭文件
                    count+=1;
                    print(count)  #统计图片个数，检验下载图片是否完整
            except :#遇到异常时，print url
                    print ("Error: "+url)
                    errolist.append(url)
                #跳过异常，继续