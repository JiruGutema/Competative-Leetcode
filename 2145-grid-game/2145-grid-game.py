class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = (prefix[i]+grid[0][i])

        suffix = [0]*(n+1)
        for i in range(n-1, -1,-1):
            suffix[i] = (suffix[i+1]+grid[1][i])

        min_score = float("inf")
        for i in range(n):
            second_robot_score = max(prefix[n] - prefix[i + 1], suffix[0] - suffix[i])
            min_score = min(min_score, second_robot_score)

        return min_score

        