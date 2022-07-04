class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        allDict = defaultdict(int)
        for i, v in enumerate(nums):
            complement = target - v
            if complement in allDict:
                return [allDict[complement], i]
            allDict[v] = i