class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):   nums[i] += nums[i-1]
                
        maxx = nums[-1]
        if maxx - nums[0] == 0:
            return 0
        
        for i in range(1, len(nums)):
            curLeft = nums[max(0, i-1)]
            curRight = maxx - nums[i]       
            if curLeft == curRight:
                return i

        return -1