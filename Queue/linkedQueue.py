# -*- coding: utf-8 -*-
from node import Node
from abstractCollection import AbstractCollection

class LinkedQueue(AbstractCollection):
    
    def __init__(self,sourceCollection = None):
        self._front = self._rear = None
        AbstractCollection.__init__(self,sourceCollection)
        
    def __iter__(self):
        current = self._front
        while current is not None:
            yield current.data
            current = current.next
            
    def peek(self):
        if self.isEmpty():
            raise KeyError('queue is empty')
        return self._front.data
    
    def clear(self):
        self._front = self._rear = None
        self._items = None
        
    def add(self,item):
        newNode = Node(item)
        if self.isEmpty():
            self._front = newNode
        else:
            self._rear.next = newNode
        self._rear = newNode
        self._size += 1
        
    def pop(self):
        if self.isEmpty():
            raise KeyError('queue is empty')
        oldItem = self._front.data
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1
        return oldItem
        
