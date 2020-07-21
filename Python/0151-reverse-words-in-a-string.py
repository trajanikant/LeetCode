class Solution:
    def reverseWords(self, s: str) -> str:
        h = s.split(' ')[::-1]
        h = [i for i in h if i != '']
        print(h)
        return(' '.join(h))
