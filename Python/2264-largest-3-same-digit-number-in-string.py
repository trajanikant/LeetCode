class Solution:
    def largestGoodInteger(self, num: str) -> str:
        cur = -1
        for i in range(len(num)-2):
            if num[i] == num[i+1] and num[i+1] == num[i+2] and int(num[i:i+3]) > cur:
                cur = int(num[i:i+3])
        if cur == -1: return ""
        return ('00' + str(cur))[-3:]