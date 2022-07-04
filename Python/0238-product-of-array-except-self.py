class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lent = len(nums)
        forward = [1] * lent
        backward = [1] * lent
        
        for i in range(1, lent):
            forward[i] = forward[i-1] * nums[i-1]
        for i in range(lent-2, -1, -1):
            backward[i] = backward[i+1] * nums[i+1]

        for i in range(lent):
            forward[i] *= backward[i]
        
        return forward