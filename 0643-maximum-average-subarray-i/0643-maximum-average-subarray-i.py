class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxTotal = sum(nums[:k])
        current = maxTotal

        for right in range(k, len(nums)):
            current += nums[right]
            current -= nums[right-k]
            maxTotal = max(maxTotal, current)
        return maxTotal/k





