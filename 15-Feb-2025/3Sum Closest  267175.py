# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        curr_t = float('inf')

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                curr_s = nums[i] + nums[left] + nums[right]

                if abs(target - curr_s) < abs(target - curr_t):
                    curr_t = curr_s

                if curr_s < target:
                    left += 1
                elif curr_s > target:
                    right -= 1
                else:
                    return curr_s

        return curr_t