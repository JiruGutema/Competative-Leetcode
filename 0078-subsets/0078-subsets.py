class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, path = [],[]

        def backtrack(idx):
            if idx == len(nums):
                ans.append(path[:])
                return
            path.append(nums[idx])
            backtrack(idx+1)
            path.pop()
            backtrack(idx+1)

        backtrack(0)
        
        return ans