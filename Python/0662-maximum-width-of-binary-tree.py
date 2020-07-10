class Solution:
    def widthOfBinaryTree(self, root):
        previous_level, previous_number, max_width = 1, 1, 0
        tree_list = deque([[previous_level,previous_number,root]])
        while tree_list:    
            [num, cur_level, node] = tree_list.popleft()
            if (cur_level > previous_level):
                previous_level, previous_number = cur_level, num
                
            max_width = max(max_width, num - previous_number + 1)
            if node.left:  tree_list.append([num*2,  cur_level+1, node.left])
            if node.right: tree_list.append([num*2+1,cur_level+1, node.right])
                
        return max_width