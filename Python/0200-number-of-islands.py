class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(stack):
            while stack:
                x, y = stack.pop()
                visited = set((x,y))
                grid[x][y] = "0" 
                pos = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for i in pos:
                    dx, dy = x + i[0], y + i[1]
                    if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] == "1":
                        grid[dx][dy] = "0"
                        stack.append([dx, dy])

    
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                print(i, j)
                if grid[i][j] == "1":
                    count += 1
                    bfs([[i,j]])
        
        return count