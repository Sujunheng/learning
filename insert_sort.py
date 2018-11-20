# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 11:25:01 2018

@author: Su.Jun
"""
import random
lists=[5,3,10,5,4,8,7,1]
count=len(lists)

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
'''
'''
    # 快速排序
#!/usr/bin/python3
#def quick_sort(lists, left, right):
    # 快速排序
left=0
right=len(lists)
if left >= right: #左边点等于右边点时，排序结束
   print(lists)
key = lists[left] #初始基准数
low = left
high = right
while left < right:
    while left < right and lists[right] >= key:
            right -= 1
    lists[left] = lists[right]
    while left < right and lists[left] <= key:
            left += 1
    lists[right] = lists[left]
lists[right] = key
#quick_sort(lists, low, left - 1)
#quick_sort(lists, left + 1, high)
print( list(lists))
    
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

c=quick_sort(lists,0,count)
'''
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
 
    
   
def random_list(n):
    生成随机数据
    :param n: 
    :return: 
    ret = []
    a1 = ['赵', '钱', '孙', '李', '邹', '吴', '郑', '王', '周']
    a2 = ['力', '好', '礼', '丽', '文', '建', '梅', '美', '高', '']
    a3 = ['强', '文', '斌', '阔', '文', '莹', '超', '云', '龙', '']
    ids = range(1001, 1001 + n)
    for i in range(n):
        name = random.choice(a1) + random.choice(a2) + random.choice(a3)
        age = random.randint(18, 60)
        dic = {'id': ids[i], 'name': name, 'age': age}
        ret.append(dic)
    return ret


def sift(data, low, high):
    i = low      # 父节点
    j = 2 * i + 1   # 左子节点
    tmp = data[i]   # 父节点值
    while j <= high:    # 子节点在节点中
        if j < high and data[j]['id'] < data[j + 1]['id']:  # 有右子节点且右节点比父节点值大
            j += 1
        if tmp['id'] < data[j]['id']:
            data[i] = data[j]   # 将父节点替换成新的子节点的值
            i = j   # 变成新的父节点
            j = 2 * i + 1   # 新的子节点
        else:
            break
    data[i] = tmp   # 将替换的父节点值赋给最终的父节点


def heap_sort(data):
    n = len(data)
    # 创建堆
    for i in range(n//2-1, -1, -1):
        sift(data, i, n-1)

    # 挨个出数
    for i in range(n-1, -1, -1):    # 从大到小
        data[0], data[i] = data[i], data[0]     # 将最后一个值与父节点交互位置
        sift(data, 0, i-1)

li = random_list(1000) # 生成数据
random.shuffle(li) # 将数据打乱
heap_sort(li)
print(li)


def MAX_Heapify(heap,HeapSize,root):#在堆中做结构调整使得父节点的值大于子节点

    left = 2*root + 1
    right = left + 1
    larger = root
    if left < HeapSize and heap[larger] < heap[left]:
        larger = left
    if right < HeapSize and heap[larger] < heap[right]:
        larger = right
    if larger != root:#如果做了堆调整则larger的值等于左节点或者右节点的，这个时候做对调值操作
        heap[larger],heap[root] = heap[root],heap[larger]
        MAX_Heapify(heap, HeapSize, larger)

def Build_MAX_Heap(heap):#构造一个堆，将堆中所有数据重新排序
    HeapSize = len(heap)#将堆的长度当独拿出来方便
    for i in range((HeapSize -2)//2,-1,-1):#从后往前出数
        MAX_Heapify(heap,HeapSize,i)

def HeapSort(heap):#将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调整过程。
    Build_MAX_Heap(heap)
    for i in range(len(heap)-1,-1,-1):
        heap[0],heap[i] = heap[i],heap[0]
        MAX_Heapify(heap, i, 0)
    return heap

if __name__ == '__main__':
    a = [30,50,57,77,62,78,94,80,84]
    print (a)
    HeapSort(a)
    print (a)
    b = [random.randint(1,1000) for i in range(1000)]
    print (b)
    HeapSort(b)
    print (b)
'''