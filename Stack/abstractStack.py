# -*- coding: utf-8 -*-
from abstractCollection import AbstractCollection

class AbstactStack(AbstractCollection):
    
    def __init__(self,sourceCollection = None):
        AbstractCollection.__init__(self,sourceCollection)
        
    def add(self,item):
        self.push(item)
