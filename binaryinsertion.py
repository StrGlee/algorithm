#!/usr/bin/env python
# encoding: utf-8

def insertion_sort_binarysearch(list):
    length = len(list)
    for i in range(1,length):
        #确定循环次数
        current_value = list[i]
        #将循环到的值赋予value
        position = i
        low = 0
        high = i-1
        print(i, low, high)
        #确定二分查找的边界，每次从list[0]到list[i-1]

        while low <= high:
            #如果不设立=，那么第一个数，high和low都是0的时候就不能够正
            #确排序
            mid = (low+high)//2
            print(list[mid],current_value,'--')
            if list[mid] > current_value:
                high = mid - 1
            else:
                low = mid + 1
        print(list, i, low, high, list[low], list[high],current_value)
        #上面这个循环终止时，已经找到了合适的位置，low=high+1
        #这里通过循环，移动出空位
        #如 1 3 2 4 5
        #经过position的循环,将2赋予了current_value，然后根据low所确
        #定的位置，调节为 1 3 3 4 5 ，在把list[low]的值换为current_value
        #即可确定为1 2 3 4 5
        while position > low:
            list[position] = list[position -1]
            position = position -1
        list[position] = current_value
        print(list, i, low, high, list[low], list[high],current_value)
    return list

list = [3, 1, 66, 12, 33, 222, 111, 14]
print(list)
print(insertion_sort_binarysearch(list))
