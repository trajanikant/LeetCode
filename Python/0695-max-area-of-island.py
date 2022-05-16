class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(i, j):
            visited = [[i, j]]
            grid[i][j] = 0
            curArea = 1
            while visited:
                x, y = visited.pop()
                ng = [[x-1, y], [x+1, y], [x, y+1], [x, y-1]]
                for a in ng:
                    newx, newy = a
                    if 0<=newx<lenx and 0<=newy<leny and grid[newx][newy] == 1:
                        visited.append(a)
                        grid[newx][newy] = 0
                        curArea += 1
            return curArea
        
        maxArea = 0
        lenx, leny = len(grid), len(grid[0])
        for i in range(lenx):
            for j in range(leny):
                if grid[i][j] == 1:
                    maxArea = max(bfs(i, j), maxArea)
        return maxArea