from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        length = float("inf")
        i = 0
        j = 0

        while j < len(nums):
            total += nums[j]
            j += 1
            
            while total >= target:  
                length = min(j - i, length)  
                total -= nums[i]  
                i += 1  
                

        if length == float("inf"):
            return 0
        else:
            return length