class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        copy = nums[:]
        k %= n
        copy = copy[n - k:] + copy[:n - k]

        for i in range(n):
            nums[i] = copy[i]