class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lenp = len(prices)
        final = 0
        
        for i in range(1, lenp):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                final += diff
        
        return final