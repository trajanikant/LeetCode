class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        radius = 2*k+1
        final = [-1] * len(nums)
        curSum = sum(nums[:2*k])
        for i in range(2*k,len(nums)):
            curSum += nums[i]
            if i >= radius-1:
                final[i-k] = curSum // radius
                curSum -= nums[i-radius+1]

        return final