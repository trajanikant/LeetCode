class Solution:
    def __init__(self, w):
        self.cumulative = w
        for i in range(1, len(w)):
            self.cumulative[i] = self.cumulative[i-1] + self.cumulative[i]
        # print(self.cumulative)
        self.maxx = self.cumulative[-1]

    def pickIndex(self):
        target = self.maxx * random.random()
        low, high = 0, len(self.cumulative)
        while low < high:
            mid = low + (high - low) // 2
            if target > self.cumulative[mid]:   low = mid + 1
            else:                               high = mid
        return low