class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        # adjList = defaultdict(list) # list of cost, node
        # for i in range(N):
        #     x1, y1 = points[i]
        #     for j in range(i+1, N):
        #         x2, y2 = points[j]
        #         dist = abs(x1-x2) + abs(y1-y2)
        #         adjList[i].append([dist, j])
        #         adjList[j].append([dist, i])

        manhattan = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        # Prim's
        res = 0
        visit = set()
        minH = [[0, 0]]
        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for j in range(N):
                if j not in visit:
                    heapq.heappush(minH, [manhattan(points[i], points[j]), j])
            # for neiCost, nei in adjList[i]:
            #     if nei not in visit:
            #         heapq.heappush(minH, [neiCost, nei])
        return res
