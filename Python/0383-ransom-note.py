class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMap = defaultdict(int)
        for i in magazine:
            hashMap[i] += 1
        for i in ransomNote:
            hashMap[i] -= 1
        
        for i in hashMap:
            if hashMap[i] < 0:
                return False
        return True