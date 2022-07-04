class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = (Counter(nums))
        print(x)
        return[i[0] for i in x.most_common(k)]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        allDict = Counter(nums)
        maxLength = allDict.most_common(1)[0][1]
        arr = [[] for _ in range(maxLength + 1)]
        allDict = allDict.items()
        
        for a, b in allDict:
            arr[b].append(a)
        
        final = [j for i in arr for j in i]
        return final[-k:]