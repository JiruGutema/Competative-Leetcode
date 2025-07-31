class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n = len(nums)
        averages = []

        while n > 0:
            nums.sort()
            min_element = nums.pop(0)
            max_element = nums.pop(-1)
            averages.append((min_element + max_element) / 2)
            n -= 2

        return min(averages)