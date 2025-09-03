class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time = []
        for timePoint in timePoints:
            h, m = map(int, timePoint.split(':'))
            mins = h * 60 + m
            time.append(mins)
        
        time.sort()
        
        res = float('inf')
        for i in range(1, len(time)):
            res = min(time[i] - time[i - 1], res)
        
        return min(res, 1440 + time[0] - time[-1])
