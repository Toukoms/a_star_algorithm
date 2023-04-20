"""
Queue to store accessible blocks

 Author: Toky
 Starting date: 16-04-2023
"""

import heapq

from src.block import Block


class OpenList:
    
    def __init__(self, start:Block):
        self.all = [start]
        
    def size(self):
        return len(self.all)
        
    def insert(self, block:Block):
        self.all.append(block)
        
    def pop(self, block):
        self.all.remove(block)
        
    def binary_pop(self, target:Block):
        self.all.sort()
        start = 0
        end = self.size() - 1
        
        while start <= end:
            mid = (end + start) // 2
            if self.all[mid] == target:
                del self.all[mid]
                return True
        
            if target < self.all[mid]:
                end = mid - 1
            else:
                start = mid + 1

        ValueError("You have trying to remove an item that not in the list")
        
    def get_priority(self):
        priority = self.all[0]
        for block in self.all:
            if block.f < priority.f:
                priority = block
        return priority