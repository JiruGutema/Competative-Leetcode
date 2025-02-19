from typing import List

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = int(1e9 + 7)
        n = len(nums)
        sums = [0] * (n + 1)  
        
        for start, end in requests:
            sums[start] += 1
            if end + 1 < n:
                sums[end + 1] -= 1
        
        for i in range(1, n):
            sums[i] += sums[i - 1]
        
        sums.pop()

        nums.sort(reverse=True)
        sums.sort(reverse=True)

        ans = sum(nums[i] * sums[i] for i in range(n)) % MOD

        return ans
