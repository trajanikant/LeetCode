class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s += '-'
        lens = len(s)
        count = 1
        allCounts = []

        for i in range(lens-1):
            if s[i] == s[i+1]:
                count += 1
            else:
                allCounts.append(count)
                count = 1

        final = 0
        for i in range(len(allCounts)-1):
            final += min(allCounts[i], allCounts[i+1])

        return final