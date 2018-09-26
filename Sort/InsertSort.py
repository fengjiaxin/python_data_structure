# -*- coding: utf-8 -*-
'''
    插入排序：
    1.在第i轮通过列表的时候（i的范围从1到n-1），第i个项应该插入到列表的前i个项之中的正确位置
    2.在第i轮之后，前i个项应该是排好序的
    3.按照顺序放好了前i-1个项，根据第i项，将i项放到合适的位置
    4.插入排序包括两个循环。
        外围的循环从1~n-1的位置，对于外部循环的每个位置i，保存该项并且从位置i-1开始内部循环
        对于内部循环的每个位置j,都将该项移动到j+1,直到找到了给保存的项（第i项）的位置
        
'''
def InsertSort(nums):
    for i in range(1,len(nums)):
        # 要插入的第i项的
        insertItems = nums[i]
        j = i - 1
        while j >= 0:
            if nums[j] > insertItems:
                nums[j+1] = nums[j]
                j -= 1
            else:
                break
        nums[j+1] = insertItems
