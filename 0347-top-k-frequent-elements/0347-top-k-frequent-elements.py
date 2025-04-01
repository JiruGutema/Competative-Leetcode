class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force

        nums = Counter(nums)
        nums = sorted(nums.items(), key=lambda key: key[1], reverse=True)
        return [num[0] for num in nums[:k]]
        