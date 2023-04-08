class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        curFlips = s.count('0')
        minCount = curFlips
        
        for i in s:
            if i == '0':    curFlips -= 1
            else:           curFlips += 1
            minCount = min(minCount, curFlips)
            
        return minCount