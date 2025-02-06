class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        possible = defaultdict(int)
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                possible[product] += 1

        ans = 0
        for count in possible.values():
            if count > 1:
                ans += count * (count - 1) * 4
        
        return ans