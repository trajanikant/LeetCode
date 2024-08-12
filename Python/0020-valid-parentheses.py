class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {')':'(', ']':'[', '}':'{'}
        stack  = []

        for i in s:
            if stack and i in bracket_dict and stack[-1] == bracket_dict[i]:
                stack.pop()
            else:
                stack.append(i)

        return len(stack) == 0