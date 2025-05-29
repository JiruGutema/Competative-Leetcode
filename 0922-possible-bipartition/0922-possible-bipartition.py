class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        clr = {}

        def dfs(node, c):
            if node in clr:
                return clr[node] == c
            clr[node] = c
            for nei in graph[node]:
                if not dfs(nei, 1 - c):
                    return False
            return True

        for node in range(1, n + 1):
            if node not in clr:
                if not dfs(node, 0):
                    return False
        return True