class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        seen = set()
        queue = deque([(0, 0, 1)])  
        seen.add((0, 0))

        def inbound(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])

        directions = [ 
            (0, 1), (1, 0), (1, 1),
            (-1, -1), (-1, 0), (0, -1),
            (1, -1), (-1, 1)
        ]

        while queue:
            row, col, length = queue.popleft()

            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return length

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if inbound(nr, nc) and grid[nr][nc] == 0 and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    queue.append((nr, nc, length + 1))

        return -1 