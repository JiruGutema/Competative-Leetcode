class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for course, pre in prerequisites:
            graph[course].append(pre)

        visited = 2
        visiting = 1
        unvisited = 0
        states = [unvisited] * numCourses
        ans = []
        hasCycle = False

        def dfs(node):
            nonlocal hasCycle
            if states[node] == visited:
                return True
            if states[node] == visiting:
                hasCycle = True
                return False

            states[node] = visiting
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            states[node] = visited
            ans.append(node)
            return True

        for i in range(numCourses):
            if states[i] == unvisited and not dfs(i):
                return []

        return ans
