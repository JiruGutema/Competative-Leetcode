
class NumArray:
    
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [0]

        for i in nums:
            self.prefix.append(self.prefix[-1]+i)
        
    def sumRange(self, left, right):
        return self.prefix[right+1]-self.prefix[left]


