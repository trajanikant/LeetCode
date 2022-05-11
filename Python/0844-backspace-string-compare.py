class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def createString(string):
            stack = []
            for i in string:
                if i == '#':
                    if stack:  stack.pop()
                else:   stack.append(i)
            return stack
        
        return createString(s) == createString(t)