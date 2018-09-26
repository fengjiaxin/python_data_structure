# -*- coding: utf-8 -*-
'''
    归并排序:
    1.计算一个列表的中间位置，并且递归的排序其左边和右边的字列表（分而治之）
    2.将两个排好序的子列表重新合并为单个的排好序的列表
    3.当子列表不能够划分的时候，停止这个过程
'''

# 合并过程，用到一个额外的数组
from arrays import Array

def mergeSort(nums):
    copyBuffer = Array(len(nums))
    mergeSortHelper(nums,copyBuffer,0,len(nums) - 1)
    
def mergeSortHelper(nums,copyBuffer,left,right):
    if left < right:
        mid = left + (right-left)//2
        mergeSortHelper(nums,copyBuffer,left,mid)
        mergeSortHelper(nums,copyBuffer,mid+1,right)
        merge(nums,copyBuffer,left,mid,right)
        
def merge(nums,copyBuffer,left,mid,right):
    index1 = left
    index2 = mid + 1
    for i in range(left,right+1):
        if index1 > mid:
            copyBuffer[i] = nums[index2]
            index2 += 1
        elif index2 > right:
            copyBuffer[i] = nums[index1]
            index1 += 1
        elif nums[index1] < nums[index2]:
            copyBuffer[i] = nums[index1]
            index1 += 1
        else:
            copyBuffer[i] = nums[index2]
            index2 += 1

    for i in range(left,right+1):
        nums[i] = copyBuffer[i]
            