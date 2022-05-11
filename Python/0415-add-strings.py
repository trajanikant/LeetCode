class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        len1, len2 = len(num1), len(num2)
        diff, maxlen = abs(len1 - len2), max(len1, len2)
        num1 = ('0' * diff + num1)[-maxlen:]
        num2 = ('0' * diff + num2)[-maxlen:]
        
        final, carry = '', 0
        for i in range(maxlen-1, -1, -1):
            cur = int(num1[i]) + int(num2[i]) + carry
            carry, rem = divmod(cur, 10)
            final += str(rem)
        if carry!= 0:   final += str(carry)
        return final[::-1]