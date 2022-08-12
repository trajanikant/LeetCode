class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)
        dp = [[0 for _ in range(len1 + 1)] for _ in range(len2 + 1)]
        
        for i in range(len2-1, -1, -1):
            for j in range(len1-1, -1, -1):
                if text2[i] == text1[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        
        return dp[0][0]