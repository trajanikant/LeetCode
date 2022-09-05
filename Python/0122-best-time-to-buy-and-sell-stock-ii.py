class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        finalProfit = 0
        
        for i in range(1, len(prices)):
            finalProfit += max(0, prices[i] - prices[i-1])
        
        return finalProfit