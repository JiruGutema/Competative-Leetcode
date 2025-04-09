class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n

        def dfs(city):
            visited[city] = True
            for neighbor in range(n):
                if isConnected[city][neighbor] and not visited[neighbor]:
                    dfs(neighbor)

        provinces = 0
        for city in range(n):
            if not visited[city]:
                dfs(city)
                provinces += 1
        
        return provinces
