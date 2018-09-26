'''
    冒泡排序：
        从列表的的开头处开始，并且比较一对数据项，直到移动到列表的末尾；
        每当成对的两项之间的顺序不正确的时候，算法就交换其位置。这个过程
        的效果就是将最大的项以冒泡的方式排到列表的末尾。然后算法从列表开
        头到倒数第二个列表项重复这一过程，依次类推，直到该算法从列表的最
        后一项开始，此时列表已经是排序好的

'''

# 简单的冒泡排序方法
# 问题是当列表本身的顺序就是比较完好的，仍然会花费复杂的时间空间来排序
def BubbleSortEasy(lyst):
    for i in range(len(lyst)):
        for j in range(len(lyst)-i-1):
            if lyst[j] > lyst[j+1]:
                lyst[j],lyst[j+1] = lyst[j+1],lyst[j]

# 改进的冒泡排序
# 如果列表是有序的，可以跳出
def BubbleSortImp(nums):
    for i in range(len(nums)):
        is_sorted = True
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                is_sorted = False
                nums[j+1],nums[j] = nums[j],nums[j+1]
        if is_sorted:
            break
        

