from typing import List

class NumArray:
    
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.array = [0] * (len(nums) + 1)
        
        for i in range(1, len(nums) + 1):
            self.array[i] = self.array[i - 1] + nums[i - 1]
    
    def sumRange(self, left: int, right: int) -> int:
        return self.array[right + 1] - self.array[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left, right)
