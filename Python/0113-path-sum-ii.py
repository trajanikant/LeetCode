# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        final = []
        def recur(curSum, curList, curNode, final):
            if curSum == targetSum and not curNode.right and not curNode.left:  final.append(curList)            
            if curNode.left:    recur(curSum + curNode.left.val, curList + [curNode.left.val], curNode.left, final)
            if curNode.right:   recur(curSum + curNode.right.val, curList + [curNode.right.val], curNode.right, final)
            
        if root:    recur(root.val, [root.val], root, final)
        return final