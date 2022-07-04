class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        totalDict = defaultdict(int)
        for i in nums:
            totalDict[i] += 1
            if totalDict[i] > 1:
                return True
        return False