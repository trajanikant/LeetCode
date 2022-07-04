class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def convertToDict(string):
            curDict = defaultdict(int)
            for i in string:
                curDict[ord(i)] += 1
            return curDict
        
        return convertToDict(s) == convertToDict(t)