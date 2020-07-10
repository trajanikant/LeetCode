class Solution:
    def nthUglyNumber(self, n: int) -> int:
        pre = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
        lastFactor = int(n ** 0.5) + 3
        #n = 12
        uglyList = []
        for i in range(lastFactor):
            for j in range(lastFactor):
                for k in range(lastFactor):
                    uglyList.append(pow(2,i) * pow(3,j) * pow(5,k))
                    
        uglyList.sort()
        
        if n < 11:
            return pre[n-1]
        
        return uglyList[n-1]