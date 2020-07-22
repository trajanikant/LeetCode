class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if (len(nums)) > 3:
            return(min((nums[-4]-nums[0]), (nums[-3]-nums[1]), (nums[-1]-nums[3]), (nums[-2]-nums[2])))
        else:
            return 0
