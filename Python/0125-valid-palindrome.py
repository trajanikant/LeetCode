class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([i for i in s.lower() if i.isalnum()])
        return s == s[::-1]