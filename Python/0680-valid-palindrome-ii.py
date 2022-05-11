class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(subString):
            return subString == subString[::-1]
        
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                removeLeft = s[:left] + s[left+1:]
                removeRight = s[:right] + s[right+1:]
                if isPalindrome(removeLeft) or isPalindrome(removeRight):
                    return True
                return False
            left += 1
            right -= 1        
        return True