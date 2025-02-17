# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums = [0] +nums
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        start = 0
        end = len(nums)-1

        for i in range(1,len(nums)):
            if nums[i-1] == nums[end] - nums[i]:
                return i-1
        return -1

