from typing import List


class Solution:
    def productExceptSelf(self, nums:List[int])->List[int]:
        n = len(nums)
        answer = [1]*n

        prefixProduct = 1
        for i in range(n):
            answer[i] = prefixProduct
            prefixProduct *= nums[i]

        suffixProduct = 1
        for i in range(n-1, -1, -1):
            answer[i] = suffixProduct 
            suffixProduct *= nums[i]
        
        return answer
