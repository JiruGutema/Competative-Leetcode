class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        res = []
    
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count:
                heapq.heappush(heap, (count, char))
        # print(heap)

        while heap:
            count, char = heapq.heappop(heap)

            if len(res) > 1 and res[-1] == res[-2] == char:
                if not heap:
                    return "".join(res)
                count2, char2 = heapq.heappop(heap)

                if count2:
                    res.append(char2)
                    count2 += 1
                if count2:
                    heapq.heappush(heap, (count2, char2))
            else:
                if count:
                    res.append(char)
                    count += 1
            if count:
                heapq.heappush(heap, (count, char))
        return "".join(res)
            

            

 