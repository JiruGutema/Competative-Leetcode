class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums = Counter(nums)
        ans = []
        for k, v in nums.items():
            if v == 2:
                ans.append(k)
        return ans