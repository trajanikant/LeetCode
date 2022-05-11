class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curSum = sum(nums[:k])
        bestSum = curSum
        for i in range(k, len(nums)):
            curSum += (nums[i] - nums[i-k])
            bestSum = max(bestSum, curSum)
        
        return bestSum / k