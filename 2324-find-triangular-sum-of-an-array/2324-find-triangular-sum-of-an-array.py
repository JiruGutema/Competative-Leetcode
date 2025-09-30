class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        nums2 = []

        while len(nums)> 1:
            for i in range(len(nums)-1):
                nums2.append((nums[i] + nums[i+1]) % 10)
            nums = nums2
            nums2 = []

        return nums[0]

