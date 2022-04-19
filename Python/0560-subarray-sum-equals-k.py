class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        totPairs = 0
        d = dict({0:1})
        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i]
            if curSum-k in d:   totPairs += d[curSum-k]
            
            if curSum in d: d[curSum] += 1
            else:   d[curSum] = 1
        return totPairs
