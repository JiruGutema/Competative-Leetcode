class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        def inbound(i, j):
            if 0 <= i < m and 0 <= j < n:
                return True
            return False

        def dfs(i, j):
            if not inbound(i, j):
                return

            if inbound(i, j) and grid[i][j] == "0":
                return

            if inbound(i, j):
                grid[i][j] = "0"
                dfs(i+1, j)
                dfs(i-1, j)

                dfs(i, j+1)
                dfs(i, j-1)

        islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)
                    
        return islands