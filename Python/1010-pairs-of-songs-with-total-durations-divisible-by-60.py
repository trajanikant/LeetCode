class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hashMap = {i:0 for i in range(60)}
        finalValue = 0

        for i in time:
            hashMap[i % 60] += 1

        for i in hashMap:
            if i <= 30:
                if i == 0 or i == 30:   finalValue += hashMap[i] * (hashMap[i] - 1) // 2
                else:                   finalValue += hashMap[i] * hashMap[60-i]

        return (finalValue)