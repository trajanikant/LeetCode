class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashMap = {i:[] for i in range(numCourses)}
        check = defaultdict(lambda:0)
        seen = set()
        
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
            return True
        
        for i in hashMap:
            if not dfs(i):
                return False
        return True               