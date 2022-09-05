class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashMap = {i:[] for i in range(numCourses)}
        check = defaultdict(lambda:0)
        seen = set()
        final = []

        for i in prerequisites:
            x, y = i
            hashMap[x].append(y)

        def dfs(curCourse):
            if check[curCourse] == 1:
                return True
            if check[curCourse] == -1:
                return False

            seen.add(curCourse)
            for i in hashMap[curCourse]:
                if i in seen or not dfs(i):
                    return False

            check[curCourse] = 1
            seen.remove(curCourse)
            final.append(curCourse)
            return True

        for i in hashMap:
            if not dfs(i):
                return []
        return final