# -*- coding: utf-8 -*-
from arrays import Array
from abstractCollection import AbstractCollection

class ArrayQueue(AbstractCollection):
    
    DEFAULT_CAPACITY = 10
    
    def __init__(self,sourceCollection  = None):
        self._items = Array(ArrayQueue.DEFAULT_CAPACITY)
        self._front = 0
        AbstractCollection.__init__(self,sourceCollection)
        
    def __iter__(self):
        index = self._front
        while index < len(self) + self._front:
            yield self._items[index%len(self._items)]
            index += 1
            
    def peek(self):
        if self.isEmpty():
            raise KeyError('queue is empty')
        return self._items[self._front]
    
    def clear(self):
        self._front = 0
        self._size = 0
        self._items = Array(ArrayQueue.DEFAULT_CAPACITY)
    
    def _resize(self,newCapacity):
        temp = Array(newCapacity)
        for i in range(len(self)):
            temp[i] = self._items[(self._front + i)%len(self)]
        self._front = 0
        self._items = temp
    
    def add(self,items):
        # 扩容
        if len(self) == len(self._items):
            self._resize(2 * len(self))
        self._items[(self._front + self._size)%len(self._items)] = items
        self._size += 1
        
    def pop(self):
        if self.isEmpty():
            raise KeyError('queue is empty')
        oldItem = self._items[self._front]
        self._front = (self._front + 1)%len(self._items)
        self._size -= 1
        return oldItem
