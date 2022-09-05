# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            pVal, qVal, rVal = p.val, q.val, root.val
            if (rVal - pVal) > 0 and (rVal - qVal) > 0:
                root = root.left
            elif (rVal - pVal) < 0 and (rVal - qVal) < 0:
                root = root.right
            else:
                return root