# -*- coding: utf-8 -*-
'''
    快速排序：
    1.首先从列表中选择一项，这一项称为基准点
    2.将列表中的项分区，以便小于基准点的所有项都移动到基准点的坐标，而剩下的
      都移动到基准点的右边。最终，基准点的位置在完全排序的列表中的最终位置
    3.分而治之。对于在基准点分割列表而形成的子列表，递归的重复这个过程。一个字列表
      包含了基准点左边的所有项，另一个列表包含了基准点右边的所有的项
    4.每次遇到少于两个项的一个子列表，就结束这个过程
'''

# 基准点选择最后一个项
# 返回的是切分后基准点所在的位置
def partion(nums,left,right):
    pivot = nums[right]
    index = left
    for i in range(left,right):
        if nums[i] < pivot:
            # 调整元素位置，使小于pivot的项调整到左边
            nums[index],nums[i] = nums[i],nums[index]
            index += 1
    nums[right],nums[index] = nums[index],nums[right]
    return index    

def quickSortHelper(nums,left,right):
    if left < right:
        pivotIndex = partion(nums,left,right)
        quickSortHelper(nums,left,pivotIndex-1)
        quickSortHelper(nums,pivotIndex+1,right)
        
def QuickSort(nums):
    quickSortHelper(nums,0,len(nums)-1)

