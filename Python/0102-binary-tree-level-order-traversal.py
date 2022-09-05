# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def dfs(curNode, depth):
            if curNode is None:     return
            hashMap[depth].append(curNode.val)
            
            if curNode.left:        dfs(curNode.left, depth+1)
            if curNode.right:       dfs(curNode.right, depth+1)
            
        hashMap = defaultdict(list)
        dfs(root, 0)
        return list(hashMap.values())