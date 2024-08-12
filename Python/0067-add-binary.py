class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return(bin(int(a, 2) + int(b, 2))[2:])

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lena, lenb = len(a), len(b)
        maxlen = max(lena, lenb)

        a = ('0' * maxlen + a)[-maxlen:][::-1]
        b = ('0' * maxlen + b)[-maxlen:][::-1]
        i = 0
        c = ['0'] * maxlen
        sum, carry = 0, 0
        while i < maxlen:
            sum = (int(a[i]) + int(b[i]) + carry) % 2
            carry = (int(a[i]) + int(b[i]) + carry) // 2
            c[i] = str(sum)
            i += 1
        
        if carry:
            c.append('1')
        return ''.join(c)[::-1]