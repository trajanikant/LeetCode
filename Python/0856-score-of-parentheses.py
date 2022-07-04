class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = ['(']
        score, i, lens = 0, 1, len(s)
        while i < lens:
            if s[i] == ')':
                if s[i-1] == '(':
                    score += 2 ** (len(stack)-1)
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
        return score