# -*- coding: utf-8 -*-
'''
    最顶层的框架
    python继承的机制和Java不同，Java是不断覆盖父类方法
    而python可以继承多个类，采用的是广度优先策略，所以方法是自底向上的
    比如self.add()方法可以在最顶层写出来，但是在实现的时候才写出这个方法
'''
class AbstractCollection(object):
    
    def __init__(self,sourceCollection = None):
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)
                
    def isEmpty(self):
        return len(self) == 0
    
    def __len__(self):
        return self._size
    
    def __str__(self):
        return '[' + ', '.join(map(str,self))+ ']'
    
    def __add__(self,other):
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result
    
    def __eq__(self,other):
        if self is other:
            return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        
        otherIter = iter(other)
        for item in self:
            if item != next(otherIter):
                return False
        return True
        