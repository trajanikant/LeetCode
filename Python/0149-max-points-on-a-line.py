class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1
        result = 2
        for i in range(n):
            cnt = collections.defaultdict(int)
            for j in range(n):
                if j != i:
                    cnt[
                        math.atan2(
                            points[j][1] - points[i][1],
                            points[j][0] - points[i][0],
                        )
                    ] += 1
            result = max(result, max(cnt.values()) + 1)
        return result