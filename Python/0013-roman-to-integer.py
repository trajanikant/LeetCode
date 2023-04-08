class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 2
        romanDict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        integer = romanDict[s[-1]]
        while i >= 0:
            if romanDict[s[i]] < romanDict[s[i+1]]:
                integer -= romanDict[s[i]]
            else:
                integer += romanDict[s[i]]
            i -= 1
        
        return integer