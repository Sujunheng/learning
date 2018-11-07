# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 18:14:22 2018

@author: su
"""
a=[3,30,71,5,9]
count=0
num=[str(x) for x in  a]
for i in range(len(num)):
    i=i-count
    if len(num[i])>1:
        for j in num[i]:
            num+=j
        num.remove(num[i])
        count+=1

a=[int(x) for x in num]
a=sorted(a,reverse=True)
print(a)
n=[str(x) for x in a]
maxn=''.join(n)
print (maxn)
            
