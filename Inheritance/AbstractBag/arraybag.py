# -*- coding: utf-8 -*-
from arrays import Array
from abstractbag import AbstractBag

class ArrayBag(AbstractBag):
    
    DEFAULT_CAPACITY = 10
    
    def __init__(self,sourceCollection = None):
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
        AbstractBag.__init__(self,sourceCollection)
        
    def __iter__(self):
        index = 0
        while index < len(self):
            yield self._items[index]
            index += 1
            
    def clear(self):
        self._size = 0
        self._items  = Array(ArrayBag.DEFAULT_CAPACITY)
        
    def add(self,item):
        if len(self) == len(self._items):
            temp = Array(2 * len(self))
            for i in range(len(self)):
                temp[i] = self._items[i]
        self._items[len(self)] = item
        self._size += 1
        
    def remove(self,item):
        if item not in self:
            raise KeyError(str(item) + ' not in bag')
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1
        for i in range(targetIndex,len(self) - 1):
            self._items[i] = self._items[i+1]
        self._size -= 1
        

