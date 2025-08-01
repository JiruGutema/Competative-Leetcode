class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        heapq.heapify(distance)

        for i in range(len(points)):
            cand = math.sqrt((points[i][0]**2 + points[i][1]**2))
            heapq.heappush(distance, (cand, points[i]))
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(distance)[1])
        return ans