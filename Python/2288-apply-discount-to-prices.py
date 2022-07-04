class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        def ifValid(word):
            if word[0] == '$' and word.count('$') < 2 and word[1:].isdigit():
                word = '$' + "%.2f" % round(float(word[1:]) / 100 * (100-discount), 2)
            return word

        return ' '.join([ifValid(i) for i in sentence.split(' ')])