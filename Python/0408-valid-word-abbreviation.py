class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        allc = []
        while i < len(abbr) and j < len(abbr):
            if abbr[i].isalpha():
                allc.append(abbr[i])
                i += 1
            else:
                j = i
                while j < len(abbr) and abbr[j].isdigit():    j += 1
                allc.append(abbr[i:j])
                i = j

        j = 0
        for i in range(len(allc)):
            if allc[i].isalpha() and j < len(word) and word[j] == allc[i]:  j += 1
            elif allc[i].isdigit():
                if allc[i][0] != '0':   j += int(allc[i])
                else:   return False
            else:       return False

        if j != len(word):  return False
        return True