class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = [0] + sorted(horizontalCuts) + [h]
        verticalCuts = [0] + sorted(verticalCuts) + [w]
        MOD = 10 ** 9 + 7
        
        maxh, maxv = [], []
        for i in range(1, len(horizontalCuts)):
            maxh.append(horizontalCuts[i] - horizontalCuts[i-1])
        
        for i in range(1, len(verticalCuts)):
            maxv.append(verticalCuts[i] - verticalCuts[i-1])
            
        maxh, maxv = max(maxh), max(maxv)
        
        return (maxh * maxv) % MOD