
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # prefix = [0] * (len(nums) + 1)

        # for i in range(len(nums)):
        #     prefix[i + 1] = nums[i] + prefix[i]
        # 
        # res = float('-inf')

        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if res < (prefix[j + 1] - prefix[i]):
        #             res = prefix[j + 1] - prefix[i]

        # return res

        from typing import List

        min_prefix = 0 
        max_sum = float('-inf')
        current_prefix = 0 

        for num in nums:
            current_prefix += num
            max_sum = max(max_sum, current_prefix - min_prefix)
            min_prefix = min(min_prefix, current_prefix)

        return max_sum

