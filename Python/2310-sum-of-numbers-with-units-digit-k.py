class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:    return 0
        for i in range(1, 11):
            cur = (k * i) % 10
            # print(cur, str(num)[-1])
            if str(cur) == str(num)[-1] and num >= k * i:
                return i
        return -1