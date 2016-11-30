from heapq import *
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.heap = []

    def push(self, x):
        self.stack.append(x)
        heappush(self.heap,x)

    def pop(self):
        if len(self.stack) > 0:
            item = self.stack.pop(len(self.stack)-1)
            self.heap.remove(item)
            heapify(self.heap)
            return item
        return None    
    
    def top(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        return None

    def getMin(self):
        if (len(self.heap) > 0):
            return self.heap[0]