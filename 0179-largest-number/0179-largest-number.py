from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert all numbers to strings
        nums_str = list(map(str, nums))
        
        # Custom sort: compare based on concatenated results
        nums_str.sort(key=lambda x: x*10, reverse=True)
        
        # Join the sorted strings
        largest_num = ''.join(nums_str)
        
        # Edge case: if the largest number is '0', return '0'
        return largest_num if largest_num[0] != '0' else '0'