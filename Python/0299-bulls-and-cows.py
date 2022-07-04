from collections import defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        mainDict = defaultdict(int)
        bulls = 0
        lens = len(secret)
        for i in range(lens):
            curs, curg = secret[i], guess[i]
            mainDict[curs] += 1
            mainDict[curg] -= 1
            
            if secret[i] == guess[i]:
                bulls += 1
                
        none = sum([abs(i) for i in mainDict.values()]) // 2
        return str(bulls) + 'A' + str(lens-bulls-none) + 'B'