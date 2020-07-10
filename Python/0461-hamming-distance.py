from operator import xor

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        x = x ^ y
        y = 0
        while x:
            y += 1
            x = x & (x - 1)
        return y