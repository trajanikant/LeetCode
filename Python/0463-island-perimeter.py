class Solution(object):
    def islandPerimeter(self, grid):
        def get_perimeter(i, j):
            nearby = (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1),
            count = 0
            for m, n in nearby:
                if m < 0 or n < 0 or m == len(grid) or n == len(grid[0]) or grid[m][n] == 0:
                    count += 1
            return count

        final_count = 0
        for a in range(len(grid)):
            for b in range(len(grid[0])):
                if grid[a][b] == 1:
                    final_count += get_perimeter(a, b)
        return final_count