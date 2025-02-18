from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ans = [1]*len(nums)

        # prefix = 1
        # suffix = 1

        # for i in range(len(nums)):
        #     ans[i] = prefix
        #     prefix *= nums[i]

        # for i in range(len(nums)-1, -1, -1):
        #     ans[i] *= suffix
        #     suffix *= nums[i]
        # return ans
        ans = []
        prefix = [1] 
        suffix = [1]

        for i in range(1, len(nums)):
            prefix.append(prefix[-1]*nums[i-1])
        
        nums_copy = nums[:][::-1]

        for i in range(1, len(nums)):
            suffix.append(suffix[-1]*nums_copy[i-1])
        suffix = suffix[::-1]

        for i in range(len(nums)):
            ans.append(prefix[i]*suffix[i])
        return(ans)