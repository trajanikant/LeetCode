class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        visited = set()
        final_dist = copy.deepcopy(mat)
        cur_list = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    cur_list.append([i, j, 0])
                    visited.add((i,j))

        while cur_list:
            curx, cury, level = cur_list.popleft()
            ps = [[-1, 0], [1, 0], [0, 1], [0,-1]]
            for j in ps:
                nx, ny = curx + j[0], cury + j[1]
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                        final_dist[nx][ny] = 1 + level
                        cur_list.append([nx, ny, 1 + level])
                        visited.add((nx, ny))
                        
        return final_dist