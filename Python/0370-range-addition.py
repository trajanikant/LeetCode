class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        hashMap = defaultdict(int)
        final = [0] * length
        cur = 0
        
        for start, end, diff in updates:
            hashMap[start] += diff
            hashMap[end+1] -= diff
    
        for i in range(length):
            cur += hashMap[i]
            final[i] += cur
        
        return final