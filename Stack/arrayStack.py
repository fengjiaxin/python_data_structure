# -*- coding: utf-8 -*-
from arrays import Array
from abstractStack import AbstactStack

class ArrayStack(AbstactStack):
    DEFAULT_CAPACITY = 10
    
    def __init__(self,sourceCollection = None):
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)
        AbstactStack.__init__(self,sourceCollection)
        
    def __iter__(self):
        index = 0
        while index < len(self):
            yield self._items[index]
            index += 1
            
    def peek(self):
        if self.isEmpty():
            raise KeyError('the stack is empty')
        return self._items[len(self) - 1]
    
    def clear(self):
        self._size = 0
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)
        
    def push(self,item):
        if len(self) == len(self._items):
            self._resize(2 * len(self))
        self._items[len(self)] = item
        self._size += 1
    
    def _resize(self,newCapacity):
        temp = Array(newCapacity)
        for i in range(len(self)):
            temp[i] = self._items[i]
        self._items = temp
        
    def pop(self):
        if self.isEmpty():
            raise KeyError('the stack is empty')
        oldItem = self._items[len(self)-1]
        self._size -= 1
        return oldItem
    
    
        
