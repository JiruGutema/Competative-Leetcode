class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        for i in range(len(nums)):
            if target == nums[i] and ans[0] == -1:
                ans[0] = i
                ans[1] = i
            elif target == nums[i]:
                ans[1] = i
        return ans