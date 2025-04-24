class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        unique_count = len(set(nums))
        total_complete_subarrays = 0
        
    
        for start in range(n):
            freq = Counter()
            distinct_in_window = 0
            
        
            for end in range(start, n):
                if freq[nums[end]] == 0:
                    distinct_in_window += 1
                freq[nums[end]] += 1
                
               
                if distinct_in_window == unique_count:
                    total_complete_subarrays += 1

        return total_complete_subarrays
