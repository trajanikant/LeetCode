# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        x = []
        ll = []
        if root == None:
            return ll
        ll.append(root)
        while len(ll) > 0:
            cur = []
            for i in range(len(ll)):
                node = ll.pop(0)
                cur.append(node.val)
                if node.left != None:
                    ll.append(node.left)
                if node.right != None:
                    ll.append(node.right)
            x.insert(0 , cur)
        return x
