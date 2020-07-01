class Solution:
    def twoSum(self, nums, target):
        hash = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if (complement in hash and hash[complement] != i):
                return (hash[complement], i)
            else:
                hash[nums[i]] = i
