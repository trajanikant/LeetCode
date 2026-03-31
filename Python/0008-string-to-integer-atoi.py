"""
Problem     : 0008. String to Integer (atoi)
Link        : https://leetcode.com/problems/string-to-integer-atoi/description/
Difficulty  : Medium
Topics      : String

3 months    : N/A
6 months    : N/A
>6 months   : N/A

Similar Qs  :
Reverse Integer (https://leetcode.com/problems/reverse-integer/),
Valid Number (https://leetcode.com/problems/valid-number/),
Check if Numbers Are Ascending in a Sentence (https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/)

Time Taken  : N/A
Date        : 2026-03-31 00:54:11
Revision    : N
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:   return 0
        if s[0] not in '0123456789-+':   return 0

        negative = s[0] == '-'
        if not s[0].isdigit():    s = s[1:]
        
        val, i, lens = 0, 0, len(s)

        while i < lens and s[i].isdigit():
            val *= 10
            val += int(s[i])
            i += 1

        return -min(val, 2 ** 31) if negative else min(val, 2 ** 31 - 1)
