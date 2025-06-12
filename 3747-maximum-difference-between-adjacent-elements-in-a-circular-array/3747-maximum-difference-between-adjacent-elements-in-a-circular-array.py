class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        
        nums.append(nums[0])
        ans = abs(nums[1] - nums[0])

        i = 0
        j = 1

        while j < len(nums):
            cand = abs(nums[j] - nums[i])
            ans = max(ans, cand)
            i += 1
            j += 1
        return ans
                
        