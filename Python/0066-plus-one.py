class Solution:
    def plusOne(self, digits):
        return list(str(int(''.join(str(i) for i in digits)) + 1))