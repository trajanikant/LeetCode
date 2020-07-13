class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        lc = len(costs)//2
        costs = sorted(costs, key=lambda x:x[0]-x[1])
        final = 0
        
        for i in range(lc):
            final += costs[i][0] + costs[lc+i][1]
            #print(final, costs[i][0], costs[lc+i][1])
            
        return final