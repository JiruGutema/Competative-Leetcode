class Solution:
    def sortArray(self, nums):
        if not nums:
            return nums

        mins, maxs = min(nums), max(nums)
        offset = -mins
        ans = [0] * (maxs - mins + 1)

        for num in nums:
            ans[num + offset] += 1

        ret = []
        for i in range(len(ans)):
            ret.extend([i - offset] * ans[i])

        return ret