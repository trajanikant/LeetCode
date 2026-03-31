"""
Problem: 1249. Minimum Remove to Make Valid Parentheses
LeetCode Link: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
Difficulty: Medium
Topics: String, Stack
Companies 3 months: N/A
Companies 6 months: N/A
Companies >6 months: N/A
Similar Questions (Top 5):
Minimum Number of Swaps to Make the String Balanced (https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/),
Check if a Parentheses String Can Be Valid (https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/)
Date: 2026-03-30 22:04:12
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