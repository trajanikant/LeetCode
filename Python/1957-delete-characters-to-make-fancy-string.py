class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        for i in s:
            if len(stack) < 2:  stack.append(i)
            else:
                if stack[-2] == i and stack[-1] == i:   continue
                else:   stack.append(i)
        
        return ''.join(stack)