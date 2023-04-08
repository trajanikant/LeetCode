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