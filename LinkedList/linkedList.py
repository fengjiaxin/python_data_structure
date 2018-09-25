# -*- coding: utf-8 -*-
from node import Node

class LinkedList(object):
    # 初始化链表为空表
    def __init__(self):
        self._head = None
        self._length = 0
        
    def isEmpty(self):
        return self._head == None
    
    # add 在链表前段插入一个元素
    def addFirst(self,value):
        newNode = Node(value)
        newNode._next = self._head
        self._head = newNode
        
    def size(self):
        return self._length
        
    # add 在链表尾部添加元素
    def append(self,value):
        newNode = Node(value)
        if self.isEmpty():
            self._head = newNode
        else:
            current = self._head
            while current._next != None:
                current = current._next
            current._next = newNode
        self._length += 1
            
    # 检测元素是否在链表中
    def search(self,data):
        current = self._head
        findFlag = False
        while current != None and not findFlag:
            if current._data == data:
                findFlag = True
            else:
                current = current._next
        return findFlag

    # remove 删除表中的某项元素
    def remove(self,value):
        # 先查看要删除的元素是否在链表中国
        pre = None
        current = self._head
        findFlag = False
        while current is not None:
            if current._data == value:
                findFlag = True
                if pre is None:
                    self._head = current._next
                else:
                    pre._next = current._next
                break
            else:
                pre = current
                current = current._next
        self._length -= 1
        if findFlag == False:
            self._length += 1
            raise ValueError('%s is not in linkedList'%value)
            
    # index 索引在链表中的位置        
    def index(self,value):
        current = self._head
        count = 1
        findFlag =False
        while current is not None and not findFlag:
            if current._data == value:
                findFlag = True
            else:
                current = current._next
                count += 1
        if findFlag:
            return count
        else:
            raise ValueError('%s is not in linkedlist'%value)
            
    # insert 链表插入元素
    def insert(self,index,value):
        if index <= 1:
            self.addFirst(value)
        elif index > self._length:
            self.append(value)
        else:
            newNode = Node(value)
            count = 1
            pre = None
            current = self._head
            while count < index:
                pre = current
                current = current._next
                count += 1
            pre._next = newNode
            newNode._next = current
        self._length += 1
            
    def __str__(self):
        result = ''
        current = self._head
        while current._next is not None:
            result += str(current._data) +  '->'
            current = current._next
        result += str(current._data)
        return result
        
        
        
