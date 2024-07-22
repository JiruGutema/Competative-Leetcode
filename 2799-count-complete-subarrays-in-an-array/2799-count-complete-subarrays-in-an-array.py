from collections import Counter
from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        unique_count = len(set(nums))
        total_complete_subarrays = 0
        
        # Iterate over each possible starting point of the subarray
        for start in range(n):
            freq = Counter()
            distinct_in_window = 0
            
            # Extend the window to the right
            for end in range(start, n):
                if freq[nums[end]] == 0:
                    distinct_in_window += 1
                freq[nums[end]] += 1
                
                # Check if the current window has the same number of distinct elements as the entire array
                if distinct_in_window == unique_count:
                    total_complete_subarrays += 1

        return total_complete_subarrays
