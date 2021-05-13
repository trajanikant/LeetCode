class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lc = len(cardPoints)
        cardPoints = cardPoints[lc-k:] + cardPoints[:k]
        #print(cardPoints)
        final = sum(cardPoints[:k])
        cur = final
        for i in range(k):
            cur += cardPoints[i+k] - cardPoints[i]
            final = max(final, cur)
            #print(i, cur, final, cardPoints[i+k], cardPoints[i])
        return final