class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x : x[1], reverse=True)
        count, i, units  = 0, 0, 0
        lens = len(boxTypes)
        
        while count < truckSize and i < lens:
            boxSize, boxCount = boxTypes[i]
            if count + boxSize < truckSize:
                count += boxSize
                i += 1
                units += boxSize * boxCount
            else:
                units += boxCount * (truckSize - count)
                count = truckSize
        
        return units