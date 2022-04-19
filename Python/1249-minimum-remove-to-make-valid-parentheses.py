class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack, s = [], list(s)
        for i in range(len(s)):
            if s[i] in ['(',')']:
                if stack:
                    if s[stack[-1]] == '(' and s[i] == ')': stack.pop()
                    else:                                   stack += i,
                else:   stack.append(i)
        
        for i in range(len(stack)-1,-1,-1):
            del s[stack[i]]
        
        return ''.join(s)