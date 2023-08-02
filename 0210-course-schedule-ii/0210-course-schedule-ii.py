class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # check cycle, check for len(ans) == numCourses return ans else []
        adj, ans = {}, []
        visited, cycle = set(), set()

        for i in range(numCourses):
            adj[i] =[]
        for p1, p2 in prerequisites:
            adj[p1].append(p2)
        print(adj)

        def dfs(c):
            if c in cycle:   
                return False
            if c in visited:
                return True

            cycle.add(c) # to avoid cycles like 0->1->0 {0:[1], 1:[2]}
            for course in adj[c]:
                if dfs(course) == False:
                    return False
            cycle.remove(c) # remove at the end once we  have travelled the path.
            visited.add(c)
            if c not in ans:
                ans.append(c)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return ans