class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parents = defaultdict(lambda:'')
        
        for i in regions:
            for j in range(1, len(i)):
                parents[i[j]] = i[0]
        
        finalSet = set({region1})
        while parents[region1]:
            finalSet.add(parents[region1])
            region1 = parents[region1]
        
        while True:
            if region2 in finalSet:
                return region2
            region2 = parents[region2]