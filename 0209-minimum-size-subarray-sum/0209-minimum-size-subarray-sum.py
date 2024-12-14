class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float('inf')
        total = 0
        i = 0
        j = 0

        while j < len(nums):
            total += nums[j]
            
            while total >= target:
                minLength = min(minLength, j - i + 1)
                total -= nums[i]
                i += 1
            j += 1

        return 0 if minLength == float('inf') else minLength

       