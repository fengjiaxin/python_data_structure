# -*- coding: utf-8 -*-
from node import Node

class LinkedBag(object):
    def __init__(self,sourceCollection = None):
        self._head = None
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)
                
    def isEmpty(self):
        return self._size == 0
    
    def __len__(self):
        return self._size
    
    def __str__(self):
        return '{' + ', '.join(map(str,self)) + '}'
    
    def __iter__(self):
        current = self._head
        while current is not None:
            yield current.data
            current = current.next
            
    def __add__(self,other):
        result = LinkedBag(self)
        for item in other:
            result.add(item)
        return result
    
    def __eq__(self,other):
        if self is other:
            return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        for item in self:
            if item not in other:
                return False
        return True
    
    def add(self,item):
        self._head = Node(item,self._head)
        self._size += 1
        
    def clear(self):
        self._head = None
        self._size = 0
        
    def remove(self,item):
        if item not in self:
            raise KeyError(str(item) + ' not in bag')
        pre = None
        current = self._head
        for targetItem in self:
            if targetItem == item:
                break
            pre = current
            current = current.next
        if pre == None:
            self._head = self._head.next
        else:
            pre.next = current.next
        self._size -= 1
        
            
            