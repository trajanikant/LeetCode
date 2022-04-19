class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        
        for i in range(len(nums)):
            # first moves through all the values
            el = nums[i]
            if el != 0:
                # this pointer keeps on incrementing when value is correctly placed
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1