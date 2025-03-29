class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans, path = [], []
        curr_sum = 0

        def backtrack(i, curr_sum):
            if curr_sum == target:

                ans.append(path[:])
                return
            elif curr_sum > target or i >= len(candidates):
                return
        
            backtrack(i+1, curr_sum)
            path.append(candidates[i])
            backtrack(i, curr_sum+candidates[i])
            path.pop()
        backtrack(0, curr_sum)
        return ans

