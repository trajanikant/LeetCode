# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        leftHeight = self.maxDepth(root.left)
        rightHeight = self.maxDepth(root.right)
        
        return max(leftHeight, rightHeight) + 1