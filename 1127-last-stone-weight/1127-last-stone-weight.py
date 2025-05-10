class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapify(heap)

        for i in range(len(stones)):
            stones[i] = -stones[i]
        for num in stones:
            heappush(heap, num)

        while heap and len(heap) >= 2:
            stone1 = heappop(heap)
            stone2 = heappop(heap)
            if stone1 == stone2:
                continue
            else:
                heappush(heap, -abs(stone1 - stone2))
        if heap:
            return -heappop(heap)
        else:
            return 0
            
