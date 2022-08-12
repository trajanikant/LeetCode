# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        exists = False
        def recur(curSum, node):
            if curSum == targetSum and not node.left and not node.right:    return True
            if node.left and recur(curSum + node.left.val, node.left):      return True
            if node.right and recur(curSum + node.right.val, node.right):   return True
        
        if root:
            exists = recur(root.val, root)
        return exists