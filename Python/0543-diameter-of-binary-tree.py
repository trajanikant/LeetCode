# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diam = 0
        
        def dfs(node):
            if not node:
                return 0
            ll = dfs(node.left)
            lr = dfs(node.right)
            self.diam = max(self.diam, lr + ll)
            return max(ll, lr) + 1
            
        dfs(root)
        return self.diam
