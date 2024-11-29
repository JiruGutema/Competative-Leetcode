
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Sort the array
        nums.sort()
        # The majority element will always be at the middle for a sorted array
        return nums[len(nums) // 2]
        