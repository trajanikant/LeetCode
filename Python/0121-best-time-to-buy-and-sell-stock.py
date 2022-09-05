class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = inf
        profit = 0
        
        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            profit = max(profit, prices[i] - minPrice)
            
        return profit