class Solution:
    def isHappy(self, n: int) -> bool:
        seenNumbers = dict()
        while n not in seenNumbers:
            seenNumbers[n] = 1
            cur = [int(j)**2 for j in str(n)]
            curSum = sum(cur)
            n = curSum
            if n == 1:  return True
        return False