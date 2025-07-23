class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        parent = list(range(n))
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return
            if rank[rootX] < rank[rootY]:
                rootX, rootY = rootY, rootX
            parent[rootY] = rootX
            rank[rootX] += rank[rootY]
            return True

        for u, v in connections:
            union(u, v)

        components = len(set(find(i) for i in range(n)))
        return components - 1
