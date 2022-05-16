from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = defaultdict()
        for i in range(len(nums)):
            cur = nums[i]
            if cur in dic and i - dic[cur] <= k:
                return True
            dic[cur] = i
        return False