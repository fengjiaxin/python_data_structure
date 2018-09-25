# -*- coding: utf-8 -*-
from arrays import Array
from arraybag import ArrayBag


class ArraySortedBag(ArrayBag):
    
    def __init__(self,sourceCollection = None):
        ArrayBag.__init__(self,sourceCollection)
    
    def __contains__(self,item):
        left = 0
        right = len(self) - 1
        while left <= right:
            mid = left + (right - left)//2
            if self._items[mid] == item:
                return True
            elif self._items[mid] < item:
                left = mid + 1
            else:
                right = mid -1
        return False
    
    def add(self,item):
        # 判断是否需要扩容
        if len(self) == len(self._items):
            temp = Array(2 * len(self))
            for i in range(len(self)):
                temp[i] = self._items[i]
            self._items = temp
        if self.isEmpty() or item > self._items[len(self) - 1]:
            ArrayBag.add(self,item)
        else:
            left = 0
            right = len(self) - 1
            # 找到第一个大于等于item的项
            while left < right:
                mid = left + (right - left)//2
                if self._items[mid] < item:
                    left = mid + 1
                else:
                    right = mid
            # left是第一个大于item的index
            for i in range(len(self),left,-1):
                self._items[i] = self._items[i-1]
            self._items[left] = item
            self._size += 1
                
    def __add__(self,other):
        result = ArraySortedBag(self)
        for item in other:
            result.add(item)
        return result