class Solution:
    def greatestLetter(self, s: str) -> str:
        lower, upper = [0] * 26, [0] *26
        for i in s:
            if ord(i) < 94:
                upper[ord(i) - ord('A')] += 1
            else:
                lower[ord(i) - ord('a')] += 1
        
        for i in range(25, -1, -1):
            if lower[i] > 0 and upper[i] > 0:
                return chr(i + ord('A'))
        return ""