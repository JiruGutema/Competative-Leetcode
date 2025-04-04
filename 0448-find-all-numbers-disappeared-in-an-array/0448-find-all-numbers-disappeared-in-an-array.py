class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # nums = set(nums)
        # ans = []
        # for i in range(1, n+1):
        #     if i not in nums:
        #         ans.append(i)
        # return ans

        # cyclic sort

        n = len(nums)
        
        
        curr = 0
        while curr < n:
            correct = nums[curr] - 1
            if 0 <= correct < n and nums[curr] != nums[correct]:
                nums[curr], nums[correct] = nums[correct], nums[curr]
            else:
                curr += 1
        
    
        ans = []
        for i in range(n):
            if nums[i] != i + 1:
                ans.append(i + 1)
        
        return ans
