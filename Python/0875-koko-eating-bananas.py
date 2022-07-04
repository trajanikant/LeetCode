class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isValid(curSpeed):
            curHours = 0
            for i in piles:
                curHours += (i-1) // curSpeed + 1
            # print('in', curSpeed, curHours)
            if curHours <= h:
                return True
            return False
            
        minSpeed, maxSpeed, final = max(sum(piles) // h, 1), max(piles), 0
        
        while minSpeed <= maxSpeed:
            mid = (minSpeed + maxSpeed) // 2
            if isValid(mid):
                maxSpeed = mid - 1
                final = mid
            else:
                minSpeed = mid + 1
            
            # print(minSpeed, maxSpeed)
        
        return final