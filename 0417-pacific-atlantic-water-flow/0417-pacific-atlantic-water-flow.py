class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        pacific, atlantic = set(), set()

        def bfs(i, j, ocean):
            if (i, j) in ocean:
                return
            ocean.add((i, j))
            q = collections.deque([(i, j)])
            while q:
                r, c = q.popleft()
                # print(r, c)
                for dr, dc in directions:
                    r1, c1 = r + dr, c + dc
                    if r1 in range(m) and c1 in range(n) and heights[r1][c1] >= heights[r][c] and (r1, c1) not in ocean:               
                        # print(heights[r1][c1], heights[r][c])
                        ocean.add((r1, c1))
                        q.append((r1, c1))

        for j in range(n):
            bfs(0, j, pacific)
            bfs(m - 1, j, atlantic)
            # print(i,j)
        for i in range(m):
            bfs(i, 0, pacific)
            bfs(i, n - 1, atlantic)

        result = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) in atlantic:
                    result.append([i, j])
        return result
