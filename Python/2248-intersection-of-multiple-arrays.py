class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        a = set(list(range(1001)))
        for i in nums:
            a = a.intersection(set(i))
        return sorted(list(a))