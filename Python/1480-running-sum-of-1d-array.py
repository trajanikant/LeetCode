class Solution(object):
    def runningSum(self, nums):
        final = nums
        
        for i in range(1, len(nums)):
            final[i] = final[i-1] + nums[i]
        
        return final