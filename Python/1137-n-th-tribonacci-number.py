class Solution:
    def tribonacci(self, n: int) -> int:
        final = [0, 1, 1]
        
        for i in range(2, n+1):
            final.append(final[i] + final[i-1] + final[i-2])
        
        # print(final)
        return final[n]