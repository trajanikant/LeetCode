class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2]
        for i in range(3, n+1):
            dp.append(dp[i-1] + dp[i-2])
        
        # print(dp)
        return dp[n]