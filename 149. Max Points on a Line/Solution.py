class Solution:

    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return len(points)

        max_points = 1

        for i in range(len(points)):
            slopes = defaultdict(int)
            for j in range(len(points)):
                if i != j:
                    # Calculate the slope
                    dy = points[j][1] - points[i][1]
                    dx = points[j][0] - points[i][0]

                    # Handle vertical lines
                    if dx == 0:
                        slope = 'inf'  # Use a string to represent vertical slope
                    else:
                        slope = dy / dx

                    slopes[slope] += 1

            # Find the maximum points that share the same slope with point[i]
            max_points_on_line = max(slopes.values(), default=0)
            max_points = max(max_points, max_points_on_line + 1)  # +1 for the current point

        return max_points