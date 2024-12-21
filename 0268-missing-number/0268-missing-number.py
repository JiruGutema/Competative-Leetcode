class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums = Counter(nums)
        for i in range(len(nums)+1):
            if i not in nums:
                return i
        