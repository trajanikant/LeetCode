class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        sums = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                sums.append(sum(nums[i:j]))

        sums.sort()

        return((sum(sums[left-1:right])) % (pow(10, 9)+7))
