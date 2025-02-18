
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
        
        prefix = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]

        res = float('-inf')  
        min_prefix = prefix[0] 

        for j in range(1, len(nums) + 1):
            res = max(res, prefix[j] - min_prefix)  
            min_prefix = min(min_prefix, prefix[j]) 

        return res


