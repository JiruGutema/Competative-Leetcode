class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # count = 0

        # def isBound(i, j):
        #     return 0 <= i < m and 0 <= j < n

        # def backtrack(i, j):
        #     nonlocal count

        #     if not isBound(i, j):
        #         return
            
        #     if i == m - 1 and j == n - 1:
        #         count += 1
        #         return
            
        #     backtrack(i + 1, j)  
        #     backtrack(i, j + 1) 
        
        # backtrack(0, 0)
        # return count

        dp = [[1]*n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

