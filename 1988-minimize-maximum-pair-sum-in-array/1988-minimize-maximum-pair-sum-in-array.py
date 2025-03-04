class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        ans = 0
        while left < right:
            curr_sum = nums[left]+nums[right]
            ans = max(ans, curr_sum)
            left += 1
            right -= 1
        return ans
        
    # 2,3  4,4  5,6 11
    # 2,4  3,4  5,6 11
    # 3,6  5,4, 4,2  9
    # 5,3 4,4   6,2  8



    