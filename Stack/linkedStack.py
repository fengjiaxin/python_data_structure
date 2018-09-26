# -*- coding: utf-8 -*-
from node import Node
from abstractStack import AbstactStack

class LinkedStack(AbstactStack):
    
    def __init__(self,sourceCollection = None):
        self._items = None
        AbstactStack.__init__(self,sourceCollection)
        
    def __iter__(self):
        
        def visitNode(node):
            if node is not None:
                tempList.append(node.data)
                visitNode(node.next)
        tempList = list()
        visitNode(self._items)
        return iter(tempList)
    
    def peek(self):
        if self.isEmpty():
            raise KeyError('the stack is empty')
        return self._items.data
    
    def clear(self):
        self._size = 0
        self._items = None
        
    def push(self,item):
        self._items = Node(item,self._items)
        self._size += 1
        
    def pop(self):
        if self.isEmpty():
            raise KeyError('the stack is empty')
        data = self._items.data
        self._items = self._items.next
        self._size -= 1
        return data