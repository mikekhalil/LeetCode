class MinStack(object):
    def __init__(self):
        self.mins = []
        self.data = []

    def push(self, x):
        if (len(self.mins) == 0) or (len(self.mins) > 0 and x <= self.mins[len(self.mins)-1]):
            self.mins.append(x)
        self.data.append(x)

    def pop(self):
        if len(self.data) > 0:
            val = self.data.pop()
            if val == self.mins[len(self.mins)-1]:
                self.mins.pop()
            return val

    def top(self):
        if len(self.data) > 0:
            return self.data[len(self.data)-1]
        
    def getMin(self):
        if len(self.mins) > 0:
            return self.mins[len(self.mins)-1]