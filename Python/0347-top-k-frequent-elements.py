class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = (Counter(nums))
        print(x)
        return[i[0] for i in x.most_common(k)]
