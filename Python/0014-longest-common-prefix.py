class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lens = len(strs) - 1
        minLen = min([len(i) for i in strs])
        i, j = lens, -1
        for j in range(minLen):
            while i > 0:
                if strs[i][j] != strs[i-1][j]:
                    return strs[i][:j]
                i -= 1
            i = lens
        return strs[0][:j+1]