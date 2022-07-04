class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        final = defaultdict(int)
        
        for i in arr:
            final[i] = final[i-difference] + 1
        
        return max(final.values())