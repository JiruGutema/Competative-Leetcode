from typing import List
from collections import defaultdict, deque

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 0
        
        adj = defaultdict(list)
        in_degree = [0] * n
        
        for u, v in edges:
            adj[u].append(v)
            in_degree[v] += 1
        
        candidates = [i for i in range(n) if in_degree[i] == 0]
        
        if len(candidates) != 1:
            return -1
        
        champ = candidates[0]
        
        visited = [False] * n
        queue = deque([champ])
        visited[champ] = True
        count = 1
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    count += 1
                    queue.append(v)
        
        return champ if count == n else -1