'''
  选择排序：
    搜索整个列表，找到最小项的位置，如果该位置不是列表的第一个位置，算法就交换这两个位置
    的项，然后算法会到第二个位置并重复这个过程，如果必要的话，将最小项和第二个位置的项交
    换。当算法达到整个过程的最后一个位置，列表就是排序好的
    
    
'''

def SelectionSort(lyst):
    for i in range(len(lyst)):
        minIndex = i
        for j in range(i+1,len(lyst)):
            if lyst[j] < lyst[minIndex]:
                minIndex = j
        if minIndex != i:
            lyst[minIndex],lyst[i] = lyst[i],lyst[minIndex]
        
        
def main():
    lyst = [4,7,5,6,1]
    print('before:'+str(lyst))
    SelectionSort(lyst)
    print('after:' + str(lyst))
    
if __name__ == '__main__':
    main()

