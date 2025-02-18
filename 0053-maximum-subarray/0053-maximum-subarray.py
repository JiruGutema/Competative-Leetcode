
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
        
        cur_sum = 0
        max_sum = nums[0]
        for ele in nums:
            if ele + cur_sum < ele:
                cur_sum = ele
            else:
                cur_sum = cur_sum + ele
            max_sum = max(max_sum, cur_sum)
        return max_sum


