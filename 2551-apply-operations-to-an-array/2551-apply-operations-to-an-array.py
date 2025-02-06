class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
                
        for num in nums:
            if num!=0:
                arr.append(num)
        for i in range(len(nums)-len(arr)):
            arr.append(0)
        return arr
