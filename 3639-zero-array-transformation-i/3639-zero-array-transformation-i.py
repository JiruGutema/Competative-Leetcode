class Solution(object):
    def isZeroArray(self, nums, queries):
        n = len(nums)
        freq = [0] * (n + 1)    
        for l, r in queries:
            freq[l] += 1
            if r + 1 < n:
                freq[r + 1] -= 1        
        count = [0] * n
        count[0] = freq[0]
        for i in range(1, n):
            count[i] = count[i - 1] + freq[i]
        for i in range(n):
            if nums[i] > count[i]:
                return False
        return True