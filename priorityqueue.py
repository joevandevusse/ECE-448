##Taken from https://www.redblobgames.com/pathfinding/a-star/implementation.html##
##Was really simple code to make a priority queue, didnt really know how to change it

import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def push(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def pop(self):
        return heapq.heappop(self.elements)[1] # 0?