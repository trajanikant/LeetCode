class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, maxRow = 0, len(matrix)
        
        while row < maxRow:
            if matrix[row][-1] >= target:
                lo, hi = 0, len(matrix[0])
                while lo <= hi:
                    mid = (lo + hi) // 2
                    if matrix[row][mid] == target:      return True
                    elif matrix[row][mid] < target:     lo = mid + 1
                    else:                               hi = mid - 1
                return False
            else:
                row += 1