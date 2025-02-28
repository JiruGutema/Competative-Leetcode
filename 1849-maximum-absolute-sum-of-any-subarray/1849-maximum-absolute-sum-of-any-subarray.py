class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        curr_sum = 0

        for num in nums:
            curr_sum = max(num, curr_sum+num)
            max_sum = max(curr_sum, max_sum)

        min_sum = float("inf")
        curr_sum = 0

        for num in nums:
            curr_sum = min(num, curr_sum+num)
            min_sum = min(curr_sum, min_sum)
        return max(abs(min_sum), max_sum)
        
        
