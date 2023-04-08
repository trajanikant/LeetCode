class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        hashMap = defaultdict(list)
        digitLogs = []
        
        for i in logs:
            curLog = i.split(' ')
            curIdentifier = curLog[0]
            curContent = ''.join(curLog[1:])
            
            if curContent.isdigit():
                digitLogs.append(i)
            else:
                hashMap[' '.join(curLog[1:])].append(curIdentifier)
        
        hashMap = sorted(hashMap.items(), key=lambda x: x[0])
        letterLogs = []
        
        for i in hashMap:
            curContent, curIdentifier = i
            for j in sorted(curIdentifier):
                letterLogs.append(j + ' ' + curContent)
        
        return letterLogs + digitLogs