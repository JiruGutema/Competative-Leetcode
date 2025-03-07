class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count = 0
        points = sorted(points, key=lambda ele: ele[1])
        i = 0
        while i < (len(points)):
            curr = points[i][1]
            while i < len(points) and curr >= points[i][0]:
                i += 1
            count += 1
        return count


