# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        hi, lo = n, 1
        while hi > lo:
            mid = (hi+lo) // 2
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
    
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(1) == True:
            return 1
        lo, hi = 1, n
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if isBadVersion(mid) is True:
                hi = mid
            else:
                lo = mid
        
        return hi