class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        p1, p2 = wordsDict.index(word1), wordsDict.index(word2)
        distance = abs(p1- p2)
                
        for i, v in enumerate(wordsDict):
            if v == word1:      p1 = i
            elif v == word2:    p2 = i
            
            distance = min(abs(p1- p2), distance)

        
        return distance