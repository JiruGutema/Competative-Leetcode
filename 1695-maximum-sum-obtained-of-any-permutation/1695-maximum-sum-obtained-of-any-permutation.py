class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        aums = [0] * n
        for start, end in requests:
            aums[start] += 1
            if end + 1 < n:
                aums[end + 1] -= 1
        for i in range(1, n):
            aums[i] += aums[i - 1]
        aums.sort(reverse=True)
        
        ans = 0
        mod = int(1e9 + 7)
        for i in range(len(nums)):
            ans += nums[i] * aums[i]
        
        return int(ans % mod)