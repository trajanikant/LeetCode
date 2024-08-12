class Solution:
    def longestPalindrome(self, s: str) -> str:
        lens = len(s)

        def maxLen(i, j):
            while i >= 0 and j < lens and s[i] == s[j]:
                i -= 1
                j += 1
            # return only even numbers - sometimes issues occur around index 0 
            return ((j - i - 2) // 2) * 2
        
        # keep storing indices and max len of palindromic string
        res = [0, 0]
        diff = res[1] - res[0]
        for i in range(lens):
            odd = maxLen(i, i)
            if diff < odd + 1:
                res = [i - odd//2, i + odd//2]
                diff = odd + 1

            # only run if adajacent chars match
            if i+1 < lens and s[i] == s[i+1]:
                even = maxLen(i, i + 1)
                if diff < even + 2:
                    res = [i - even//2, i + 1 + even//2]
                    diff = even + 2
            
        return s[res[0] : res[1] + 1]
            