"""
Problem: 0124. Binary Tree Maximum Path Sum
LeetCode Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
Difficulty: Hard
Topics: Dynamic Programming, Tree, Depth-First Search, Binary Tree
Companies 3 months: N/A
Companies 6 months: N/A
Companies >6 months: N/A
Similar Questions (Top 5):
Path Sum (https://leetcode.com/problems/path-sum/),
Sum Root to Leaf Numbers (https://leetcode.com/problems/sum-root-to-leaf-numbers/),
Path Sum IV (https://leetcode.com/problems/path-sum-iv/),
Longest Univalue Path (https://leetcode.com/problems/longest-univalue-path/),
Time Needed to Inform All Employees (https://leetcode.com/problems/time-needed-to-inform-all-employees/)
Date: 2026-03-30 21:52:17
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
                
        def dfs(node):
            nonlocal maxSum
            if not node:    return 0
            
            lPath = max(dfs(node.left), 0)
            rPath = max(dfs(node.right), 0)
            
            curVal = lPath + rPath + node.val
            maxSum = max(curVal, maxSum)
            
            return node.val + max(lPath, rPath)
            
            
        maxSum = float('-inf')
        dfs(root)
        return maxSum