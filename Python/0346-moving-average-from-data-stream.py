from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.dq = deque()
        self.totSum = 0
        self.curItems = 0

    def next(self, val: int) -> float:
        self.dq.append(val)
        self.totSum += val
        
        if self.curItems >= self.size:  self.totSum -= self.dq.popleft()
        else:                           self.curItems += 1
            
        return self.totSum / self.curItems


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)