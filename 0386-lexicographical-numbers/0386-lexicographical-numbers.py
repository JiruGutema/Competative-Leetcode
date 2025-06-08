class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        space = []
        for i in range(1,n+1):
            heapq.heappush(space, str(i))
        ans = []

        while space:
            ans.append(int(heapq.heappop(space)))
        return ans


