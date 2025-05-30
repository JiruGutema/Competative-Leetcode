class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):
            count = 0
            for num in nums:
                count += (num >> i) & 1
            if count % 3:
                result |= (1 << i)
        if result >= 2**31:
            result -= 2**32
        return result
    