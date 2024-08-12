class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashMap = defaultdict(int)
        for i in s:
            hashMap[i] += 1
        
        final, counter = 0, 0 
        for i in hashMap:
            if hashMap[i] % 2 == 0:
                final += hashMap[i]
            else:
                final += hashMap[i] - 1
                if counter != 1:
                    final += 1
                counter = 1
        
        return final