class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkBoxes(r,c):
            curHash = defaultdict(int)
            for i in range(3*r, 3*(r+1)):
                for j in range(3*c, 3*(c+1)):
                    curVal = board[i][j]
                    if curVal.isdigit():
                        curHash[curVal] += 1
                        print(curVal, curHash, curHash[curVal] > 1)
                        if curHash[curVal] > 1: return False
            return True
        
        for i in range(3):
            for j in range(3):
                if not checkBoxes(i,j): return False
        
        for i in range(9):
            curHash = defaultdict(int)
            curHash2 = defaultdict(int)
            for j in range(9):
                curVal = board[i][j]
                curVal2 = board[j][i]
                if curVal.isdigit():
                    curHash[curVal] += 1
                    if curHash[curVal] > 1:     return False
                if curVal2.isdigit():
                    curHash2[curVal2] += 1
                    if curHash2[curVal2] > 1:     return False
        
        return True