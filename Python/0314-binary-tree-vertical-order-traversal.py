# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:    return []
        stack = deque([(root, 0)])
        hashMap = defaultdict(list)
        while stack:
            curNode, level = stack.popleft()
            hashMap[level].append(curNode.val)
            leftNode = curNode.left
            rightNode = curNode.right
            if leftNode != None:       stack.append((leftNode, level-1))
            if rightNode != None:      stack.append((rightNode, level+1))
        
        hashMap = sorted(hashMap.items(), key = lambda i: i[0])
        final = [i[1] for i in hashMap]
        
        return final