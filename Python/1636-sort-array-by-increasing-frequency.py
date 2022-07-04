class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hashMap = defaultdict(int)   
        listHash = defaultdict(list)
        final = []
        
        for i in nums:  hashMap[i] += 1
        hashMap = sorted(hashMap.items(), key = lambda x : x[1])
        
        for a, b in hashMap:
            listHash[b].append(a)
        
        for i in listHash:
            for j in sorted(listHash[i], reverse = True):
                final.extend([j]*i)
                
        return final