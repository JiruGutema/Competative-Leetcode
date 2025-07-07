class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        
#         q = deque([0])
#         seen = set()
#         steps = [x, -x, y, -y]

#         while q:
#             cur = q.popleft()
#             for step in steps:
#                 tot = cur + step 
#                 if tot == z:
#                     return True
#                 if tot not in seen and 0 <= tot <= x + y:
#                     seen.add(tot)
#                     q.append(tot)
#         return False

        if z > x + y:
            return False

        visited = set()
        queue = deque()
        queue.append((0, 0))  # (jugX, jugY)

        while queue:
            a, b = queue.popleft()

            if a + b == z or a == z or b == z:
                return True

            if (a, b) in visited:
                continue

            visited.add((a, b))

            # All possible operations
            next_states = [
                (x, b),       # Fill jug X
                (a, y),       # Fill jug Y
                (0, b),       # Empty jug X
                (a, 0),       # Empty jug Y
                # Pour X -> Y
                (a - min(a, y - b), b + min(a, y - b)),
                # Pour Y -> X
                (a + min(b, x - a), b - min(b, x - a)),
            ]

            for state in next_states:
                if state not in visited:
                    queue.append(state)

        return False
