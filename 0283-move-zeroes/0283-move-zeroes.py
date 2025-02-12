class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s, p = 0, 0

        while s < len(nums) and p < len(nums):
            if nums[s] != 0:
                nums[p], nums[s] = nums[s], nums[p]
                p += 1
            s += 1

        