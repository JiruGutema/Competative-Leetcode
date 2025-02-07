class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = 0
        left_over = 0

        counter = Counter(nums)

        for v in counter.values():
            count += v//2
            left_over += v%2
        return [count, left_over]