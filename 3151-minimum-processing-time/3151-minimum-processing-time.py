class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)

        i = 3
        j = 0
        res = 0

        while i < len(tasks):
            curr = processorTime[j]+tasks[i]
            res = max(res, curr)
            j += 1
            i += 4
        return res

