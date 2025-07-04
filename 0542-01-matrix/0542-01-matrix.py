class Solution:
    def updateMatrix(self, mat):
        m, n = len(mat), len(mat[0])
        ans = [[0] * n for _ in range(m)]
        visited = [[0] * n for _ in range(m)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    visited[i][j] = 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            r, c, l = q.popleft()
            ans[r][c] = l
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    q.append((nr, nc, l + 1))

        return ans