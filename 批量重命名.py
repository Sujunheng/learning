# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 14:50:33 2018

@author: Su.Jun
"""

import os
path='D:/WORK/第十五周/hudamodeltext/hudadata_pic/huda/'   

#获取该目录下所有文件，存入列表中
f=os.listdir(path)
print(f)
n=len(f)
for i in range(n):
    try:
    #设置旧文件名（就是路径+文件名）
        ff=f[i].split('_')
        oldname=path+f[i]
    #print(f[n])
    #设置新文件名
        newname=path+ff[0]+'_'+ff[1]+'-'+ff[2]
    
    #用os模块中的rename方法对文件改名
        os.rename(oldname,newname)
        print(oldname,'======>',newname)
        n+=1
    except:
        print('erro:'+oldname)