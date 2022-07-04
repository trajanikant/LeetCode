class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lent = len(temperatures)
        final = [0] * lent
        stack, i = [[0, temperatures[0]]], 1
        
        while i < lent:            
            while stack and stack[-1][-1] < temperatures[i]:
                a, b = stack.pop()
                final[a] = i-a
            
            stack.append([i, temperatures[i]])
            i += 1
        
        return final