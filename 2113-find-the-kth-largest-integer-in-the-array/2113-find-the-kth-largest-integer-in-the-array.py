class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        num = [int(i) for i in nums]

        num = sorted(num, reverse=True)
        return str(num[k-1])