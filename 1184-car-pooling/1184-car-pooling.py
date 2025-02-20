class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix = [0]*1001

        for i in range(len(trips)):
            trip = trips[i]
            prefix[trip[1]] += trip[0]
            prefix[trip[2]] -= trip[0]

        for i in range(1, len(prefix)):
            prefix[i] = prefix[i] + prefix[i-1]

        for tot in prefix:
            if tot > capacity:
                return(False)
                break 
        else:
            return(True)