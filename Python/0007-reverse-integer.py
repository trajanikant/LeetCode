"""
Problem     : 0007. Reverse Integer
Link        : https://leetcode.com/problems/reverse-integer/description/
Difficulty  : Medium
Topics      : Math

3 months    : N/A
6 months    : N/A
>6 months   : N/A

Similar Qs  :
String to Integer (atoi) (https://leetcode.com/problems/string-to-integer-atoi/),
Reverse Bits (https://leetcode.com/problems/reverse-bits/),
A Number After a Double Reversal (https://leetcode.com/problems/a-number-after-a-double-reversal/),
Count Number of Distinct Integers After Reverse Operations (https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/)

Time Taken  : N/A
Date        : 2026-03-31 00:53:33
Revision    : N
"""


class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        if negative:    x = -x
        reverse = 0
        while x > 0:
            reverse *= 10
            reverse += x % 10
            x //= 10
            
        if reverse > 2 ** 31 - 1:   return 0

        return -reverse if negative else reverse