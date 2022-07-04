class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        lens = len(s)-1
        final, i, curValue = 0, 0, 0
        
        while lens > -1:
            if s[lens] == '1' and curValue+2 ** i <= k:
                curValue += 2 ** i
                final += 1
                
            if s[lens] == '0':
                final += 1
            lens -= 1
            i += 1
        return final