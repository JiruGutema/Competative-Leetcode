class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = ''
        for i in digits:
            nums += str(i)
        nums = int(nums) + 1
        nums = str(nums)
        digits = []
        for i in range(len(nums)):
            digits.append(int(nums[i]))
        return digits