class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:   return 0
        hashMap = defaultdict(lambda: -1)
        maxLen, lens, left = 0, len(s), 0 

        for i in range(lens):
            cur_char = s[i]
            if hashMap[cur_char] != -1:
                left = max(left, hashMap[cur_char])
            maxLen = max(maxLen, i - left + 1)
            hashMap[cur_char] = i + 1

        return maxLen