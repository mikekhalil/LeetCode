'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
'''
class MovingAverage(object):
    def __init__(self, size):
        self.sum = 0
        self.size = size
        self.arr = []

    def next(self, val):
        if len(self.arr) == self.size:
           removed = self.arr.pop(0)
           self.sum -= removed
        self.arr.append(val)
        self.sum += val
        return self.sum / float(len(self.arr))