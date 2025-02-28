class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        curr_sum1 = 0
        min_sum = float("inf")
        curr_sum2 = 0

        for num in nums:
            curr_sum1 = max(num, curr_sum1+num)
            max_sum = max(curr_sum1, max_sum)
            curr_sum2 = min(num, curr_sum2+num)
            min_sum = min(curr_sum2, min_sum)
        return max(abs(min_sum), max_sum)
        
        
