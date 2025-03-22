class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        n = len(nums)

        def backtrack(idx):
            if idx == n:
                res.append(path[:])
                return
            path.append(nums[idx])
            backtrack(idx+1)
            path.pop()
            backtrack(idx+1)

        backtrack(0)

        return res
