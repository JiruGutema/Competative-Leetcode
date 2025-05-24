class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []

        def backtrack(start, total):
            if total == target:
                ans.append(path[:])
                return
            if total > target:
                return

            prev = -1
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue 

                path.append(candidates[i])
                backtrack(i + 1, total + candidates[i])
                path.pop()

                prev = candidates[i]

        backtrack(0, 0)
        return ans
