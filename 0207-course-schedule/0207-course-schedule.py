class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for course, pre in prerequisites:
            graph[course].append(pre)
        visited = 2
        visiting = 1
        unvisited = 0

        states = [unvisited]*numCourses

        def dfs(node):
            state = states[node]
            if state == visited:
                return True
            elif state == visiting:
                return False
            elif state == unvisited:
                states[node] = visiting
                for n in graph[node]:
                    if not dfs(n): return False
                states[node] = visited
                return True
                

        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True



        