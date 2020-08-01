class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        x1 = word.lower()
        x2 = word.upper()
        x3 = word.istitle()

        if x1 == word or x2 == word or x3 == True:
            return True
        else:
            return False
