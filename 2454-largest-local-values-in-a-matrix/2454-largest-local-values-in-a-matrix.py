class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        ans=[[0]*(n-2) for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                ans[i][j]=grid[i][j]
                for di in range(3):
                    for dj in range(3):
                        ans[i][j]=max(ans[i][j],grid[i+di][j+dj])
        return ans                