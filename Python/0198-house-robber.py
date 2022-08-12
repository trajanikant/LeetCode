class Solution:
    def rob(self, nums: List[int]) -> int:
        lenn = len(nums)
        memo = [nums[0]] * (lenn)
        if lenn > 1:
            memo[1] = max(memo[0], nums[1])

            for i in range(2, lenn):
                memo[i] = max(memo[i-1], memo[i-2] + nums[i])

        return memo[-1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        lenn = len(nums)        
        dp = [0] * (lenn+1)
        dp[lenn-1], dp[lenn] = nums[lenn-1], 0
        
        for i in range(lenn-2, -1, -1):
            dp[i] = max(dp[i+1], nums[i] + dp[i+2])
        
        return max(dp[:2])