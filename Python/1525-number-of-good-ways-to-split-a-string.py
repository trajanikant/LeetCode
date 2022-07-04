class Solution:
    def numSplits(self, s: str) -> int:
        final = 0
        dict1, dict2 = defaultdict(int), defaultdict(int)
        for i in s:
            dict2[i] += 1
        
        for i in range(len(s)):
            dict1[s[i]] += 1
            dict2[s[i]] -= 1
            if dict2[s[i]] == 0:
                dict2.pop(s[i])
            
            if len(dict2) == len(dict1):
                final += 1
            
        return final