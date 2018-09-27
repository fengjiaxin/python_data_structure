# -*- coding: utf-8 -*-
'''
    队列的模板文件

'''

class QueueInterface(object):
    
    def __init__(self,sourceCollection= None):
        pass
    
    def isEmpty(self):
        return True
    
    def __len__(self):
        return 0
    
    def __str__(self):
        return ''
    
    def __iter__(self):
        return None
    
    def __add__(self,other):
        return None
    
    def __eq__(self,other):
        return False
    
    def peek(self):
        return None
    
    def clear(self):
        pass
    
    def add(self,item):
        pass
    
    def pop(self):
        return None
