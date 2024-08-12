class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        current = [[sr,sc]]
        orig_color = image[sr][sc]
        m, n = len(image), len(image[0])

        while current:
            curx, cury = current.pop()
            image[curx][cury] = color
            visited.add((curx, cury))
            for i in [[-1,0],[1,0],[0,1],[0,-1]]:
                newx, newy = curx + i[0], cury + i[1]
                if 0 <= newx < m and 0 <= newy < n and image[newx][newy] == orig_color and (newx, newy) not in visited:
                    current.append([newx, newy])

        return image