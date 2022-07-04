class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        hashMap = defaultdict(int)
        maxx = max(nums)        
        for i in range(len(nums)):
            hashMap[nums[i]] += nums[i]        
        
        dp = [0] * (maxx+1)
        dp[1] = hashMap[1]
        
        for i in range(2, maxx+1):
            dp[i] = max(dp[i-1], hashMap[i] + dp[i-2])
        
        return max(dp[-2:])