# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        final = defaultdict(list)
        def dfs(node, level):
            if not node:
                return level

            right = dfs(node.right, level)
            left = dfs(node.left, level)
            level = max(right, left)
            final[level].append(node.val)
            return level + 1

        dfs(root, 0)
        return final.values()