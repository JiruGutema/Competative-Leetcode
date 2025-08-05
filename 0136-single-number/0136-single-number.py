class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # for i in range(len(nums)):
        #     temp = nums[0]
        #     nums.remove(nums[0])
        #     if temp not in nums:
        #         return temp
        #     else:
        #         nums.append(temp)
        a = 0
        for num in nums:
            a ^= num
        return a

# O(n)
# O(1)