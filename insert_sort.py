# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 11:25:01 2018

@author: Su.Jun
"""
lists=[5,3,10,5,4,8,7,1]

'''
#insert_sort 插入排序 腾出一个空杯子
count = len(lists)

for i in range(1, count):
   key = lists[i]
   j = i - 1
   print(i,j)
   while j >= 0:
            if lists[j] > key:
                lists[j+1] = lists[j]
                lists[j] = key
            j -= 1
            print(list(lists))
print(list)

#冒泡排序 两两比较
for i in range (0,count):
    for j in range(i+1,count):
        if lists[i]>lists[j]:
            lists[i],lists[j]=lists[j],lists[i]
        print(list(lists))


#shell排序
    # 希尔排序
count = len(lists)
step = 2
group = count // step
while group > 0:
    for i in range(0, group):
        j = i + group
        while j < count:
           k = j - group
           key = lists[j]
           while k >= 0:
               if lists[k] > key:
                   lists[k + group] = lists[k]
                   lists[k] = key
               k -= group
           j += group
    group //= step
print( list(lists))


    # 快速排序
#!/usr/bin/python3
L=[5,3,10,5,4,8,7,1]
def quick_sort(L, left, right):
    if left <= right:
        key = L[left]
        i = left
        j = right
        print(i,j)
        while i < j:
            print(list(L))
            while i < j and key <= L[j]:
                j -= 1
            L[i] = L[j]
            print(L[i],L[j])
            while i < j and L[i] <= key:
                i += 1
            L[j] = L[i]
        
        L[i] = key
        quick_sort(L, left, i - 1)
        print(list(L))
        quick_sort(L, i + 1, right)
        print(list(L))

if __name__ == '__main__':
    left=0
    right=len(L)-1
    quick_sort(L,left,right)
    
    
'''


def quick_sort(alist, start, end):
    """快速排序
    #在对快速排序优化的时候牢记一点：能够将列表均衡分开的标定点才是好的标定点。均匀分开意味着保持logn的复杂度。
    #这里我并没有实现单路快排
    快速排序是一种常用的排序算法，比选择排序快得多。例如，C语言标准库中的函数qsort 实现的就是快速排序。快速排序也使用了D&C。(分而治之)
    (1) 找出简单的基线条件;
    (2) 确定如何缩小问题的规模，使其符合基线条件。
    D&C并非可用于解决问题的算法，而是一种解决问题的思路。我们再来看一个例子。 给定一个数字数组。
    """

    # 递归的退出条件
    if start >= end:
        return

    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]

    # low为序列左边的由左向右移动的游标
    low = start

    # high为序列右边的由右向左移动的游标
    high = end

    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]

        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        alist[high] = alist[low]

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid

    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low-1)

    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low+1, end)

if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    quick_sort(alist,0,len(alist)-1)
    print(alist)



递归

def quicksort(data):
    left = 0
    right = len(data) - 1
    # 
    if left > right:
        return

    quick_sort_x(data, left, right)


def quick_sort_x(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        quick_sort_x(data, left, mid - 1)
        quick_sort_x(data, mid + 1, right)

def partition(data, left, right):
    tmp = data[left]
    while left < right:
        while left < right and data[right] >= tmp:
            right -= 1
        data[left] = data[right]

        while left < right and data[left] <= tmp:
            left += 1
        data[right] = data[left]

    data[left] = tmp
    return left

    