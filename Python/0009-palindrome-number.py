"""
Problem     : 0009. Palindrome Number
Link        : https://leetcode.com/problems/palindrome-number/description/
Difficulty  : Easy
Topics      : Math

3 months    : N/A
6 months    : N/A
>6 months   : N/A

Similar Qs  :
Palindrome Linked List (https://leetcode.com/problems/palindrome-linked-list/),
Find Palindrome With Fixed Length (https://leetcode.com/problems/find-palindrome-with-fixed-length/),
Strictly Palindromic Number (https://leetcode.com/problems/strictly-palindromic-number/),
  Count Symmetric Integers (https://leetcode.com/problems/count-symmetric-integers/),
Find the Count of Good Integers (https://leetcode.com/problems/find-the-count-of-good-integers/)

Time Taken  : N/A
Date        : 2026-03-31 00:55:40
Revision    : N
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return str(x) == str(x)[::-1]

        final, y = 0, x
        while x > 0:
            final += x % 10
            final *= 10
            x //= 10
        
        return final//10 == y