"""
Problem     : 1249. Minimum Remove to Make Valid Parentheses
Link        : https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
Difficulty  : Medium
Topics      : String, Stack

3 months    : 
6 months    : 
>6 months   : 

Similar Qs  :
Minimum Number of Swaps to Make the String Balanced (https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/),
Check if a Parentheses String Can Be Valid (https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/)

Time Taken  : N/A
Date        : 2026-03-31 00:41:58
Revision    : N
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack, s = [], list(s)
        for i in range(len(s)):
            if s[i] in ['(',')']:
                if stack:
                    if s[stack[-1]] == '(' and s[i] == ')': stack.pop()
                    else:                                   stack += i,
                else:   stack.append(i)
        
        for i in range(len(stack)-1,-1,-1):
            del s[stack[i]]
        
        return ''.join(s)