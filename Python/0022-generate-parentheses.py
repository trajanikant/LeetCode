class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(curString, left, right, curLen):
            if curLen == n*2:
                final.append(''.join(curString))
                return
            else:
                if left < n:
                    curString.append('(')
                    backtrack(curString, left+1, right, curLen+1)
                    curString.pop()
                if right < left:
                    curString.append(')')
                    backtrack(curString, left, right+1, curLen+1)
                    curString.pop()
        
        final = []
        backtrack([], 0, 0, 0)

        return final