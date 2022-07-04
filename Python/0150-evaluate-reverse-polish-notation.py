class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calculate(a, b, string):
            if string == '+':   return a + b
            if string == '-':   return b - a
            if string == '*':   return a * b
            if string == '/':   return int(b / a)
        
        stack = []
        i, lent = 0, len(tokens)
        while i < lent:
            if tokens[i].replace('-','').isdigit():
                stack.append(int(tokens[i]))
            else:
                res = calculate(stack.pop(), stack.pop(), tokens[i])
                stack .append(res)

            i += 1
            # print(stack)
        return stack.pop()