# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(curNode, path):
            if curNode is None:                 return
            if curNode == p or curNode == q:    allPaths.append(path)
            if curNode.left:                    dfs(curNode.left, path+'L')
            if curNode.right:                   dfs(curNode.right, path+'R')
            
        allPaths, i = [], 0
        dfs(root, '')
        minLen = min([len(i) for i in allPaths])
                
        while i < minLen:
            curPath1 = allPaths[0][i]
            curPath2 = allPaths[1][i]
            
            if curPath1 == curPath2 == 'L':     root = root.left
            elif curPath1 == curPath2 == 'R':   root = root.right
            else:                               break
            
            i += 1

        return root