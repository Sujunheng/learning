# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 10:46:39 2018

@author: Su.Jun
"""

s="anagram"
t='nagaram'
pattern = "abba" 
strr = "dog cat cat dog"

dic1, dic2 = {}, {}
for item in s:
   dic1[item] = dic1.get(item, 0) + 1
   
a=sorted(zip(s,t))
print (a)
    
