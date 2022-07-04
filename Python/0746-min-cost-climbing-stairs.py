class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        final = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            final.append(min(final[-1], final[-2]) + cost[i])
                
        return min(final[-1], final[-2])