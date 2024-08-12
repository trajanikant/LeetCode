class Solution:
    def trap(self, height: List[int]) -> int:
        lens, final = len(height), 0 
        rl, lr = height.copy(), height.copy()

        for i in range(1, lens):
            rl[i] = max(rl[i-1], rl[i])        
        for i in range(lens-2, -1, -1):
            lr[i] = max(lr[i+1], lr[i])        
        for i in range(1, lens-1):
            final += min(rl[i], lr[i]) - height[i]
        
        return final