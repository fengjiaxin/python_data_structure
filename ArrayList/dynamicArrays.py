# -*- coding: utf-8 -*-
from arrays import Array

class DynamicArray(object):
    def __init__(self):
        self._logicalSize = 0
        self._capacity = 10
        self._items = Array(self._capacity)
        
    def __len__(self):
        return self._logicalSize
    
    def is_empty(self):
        return self._logicalSize == 0
    
    def __getitem__(self,index):
        if not 0 <= index < self._logicalSize:
            raise ValueError('invalid index')
        return self._items[index]
    
    # 扩容
    def _resize(self,new_capacity):
        items = Array(new_capacity)
        for index in range(self._logicalSize) :
            items[index] = self._items[index]
        self._items = items
        self._capacity = new_capacity
        
    
    def add(self,value):
        if self._logicalSize == self._capacity:
            self._resize(2 * self._capacity)
        self._items[self._logicalSize] = value
        self._logicalSize += 1
        
    def insert(self,index,value):
        if self._logicalSize == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._logicalSize,index,-1):
            self._items[j] = self._items[j-1]
        self._items[index] = value
        self._logicalSize += 1
        
    def remove(self,value):
        for k in range(self._logicalSize):
            if self._items[k] == value:
                for j in range(k,self._logicalSize-1):
                    self._items[j] = self._items[j + 1]
                self._items[self._logicalSize] = None
                self._logicalSize -= 1
                return 
        raise ValueError('value not found')
        
    def _print(self):
        for i in range(self._logicalSize):
            print(self._items[i], end = ' ')
        print()
            

        
    
