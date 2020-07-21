class Solution:
    def findOrder(self, numCourses, prerequisites):
        self.adjacency_list = defaultdict(set)
        for i, j in prerequisites:
            self.adjacency_list[i].add(j)

        print(self.adjacency_list)
        self.Visited = [0] * numCourses
        self.Ans, self.FoundCycle = [], 0

        for i in range(numCourses):
            if self.FoundCycle == 1:
                break
            if self.Visited[i] == 0:
                self.dfs(i)

        if self.FoundCycle == 1:
            return []

        else:
            return(self.Ans)

    def dfs(self, new_course):
        if self.FoundCycle == 1:
            return
        if self.Visited[new_course] == 1:
            self.FoundCycle = 1
        if self.Visited[new_course] == 0:
            self.Visited[new_course] = 1
            for next_courses in self.adjacency_list[new_course]:
                self.dfs(next_courses)
            self.Visited[new_course] = 2
            self.Ans.append(new_course)
