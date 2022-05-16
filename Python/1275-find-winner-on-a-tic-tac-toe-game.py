import numpy as np

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def allPossiblities(mat):
            sum1 = np.sum(mat, axis = 1)
            sum2 = np.sum(mat, axis = 0) 
            diag1 = mat[0][0] + mat[1][1] + mat[2][2]
            diag2 = mat[2][0] + mat[1][1] + mat[0][2]
            finalList = np.concatenate([sum1, sum2, [diag1, diag2]])
            if np.in1d(3, finalList):       return 'A'
            elif np.in1d(-3, finalList):    return 'B'
            return ''

        mat = np.array([[0]*9]).reshape(3,-1)
        for i in range(len(moves)):
            curx, cury = moves[i]
            if i%2 == 0:    mat[curx][cury] = 1
            else:           mat[curx][cury] = -1
        
        allP = allPossiblities(mat)
        
        if '' != allP:      return allP
        if len(moves) < 9:  return 'Pending'
        return 'Draw'