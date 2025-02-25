from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        
        cumulative_sum = 0
        sum_map = {0: -1} 
        
        for i in range(len(nums)):
            cumulative_sum += nums[i]
            if k != 0:  
                cumulative_sum %= k
            
            if cumulative_sum in sum_map:
                if i - sum_map[cumulative_sum] > 1:
                    return True
            else:
                sum_map[cumulative_sum] = i
            
        return False