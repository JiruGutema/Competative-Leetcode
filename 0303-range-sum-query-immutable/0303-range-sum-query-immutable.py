class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        nums.insert(0, 0)
        for i in range(1, len(nums)):
            self.nums[i] += self.nums[i - 1]


    def sumRange(self, left: int, right: int) -> int:
            return self.nums[right+1] - self.nums[left]
