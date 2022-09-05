class Solution:
    def minimumMountainRemovals(self, nums):
        def LIS(nums):
            dp = [10**10] * (len(nums) + 1)
            lens = [0]*len(nums)
            for i, elem in enumerate(nums): 
                lens[i] = bisect_left(dp, elem) + 1
                dp[lens[i] - 1] = elem 
            return lens
        
        l1, l2 = LIS(nums), LIS(nums[::-1])[::-1]
        ans, n = 0, len(nums)
        for i in range(n):
            if l1[i] > 1 and l2[i] > 1:
                ans = max(ans, l1[i] + l2[i] - 1)
                
        return n - ans