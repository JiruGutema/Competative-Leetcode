class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        pr_sm = [0] * n
        sf_sum = [0] * n

        pr_sm[0] = nums[0]
        sf_sum[n - 1] = nums[n - 1]

        for i in range(1, n):
            pr_sm[i] = pr_sm[i - 1] + nums[i]
            sf_sum[n - i - 1] = sf_sum[n - i] + nums[n - i - 1]

        for i in range(n):
            dif = ((nums[i] * i) - pr_sm[i]) + (sf_sum[i] - (nums[i] * (n - i - 1)))
            result[i] = dif

        return result