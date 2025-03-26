class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans, path = [], []

        def backtrack(n):
            if n == len(nums) and len(path) == len(nums):
                ans.append("".join(path[:]))
                return
            elif n == len(nums):
                return
            
            path.append("1")
            backtrack(n+1)
            path.pop()
            path.append("0")
            backtrack(n+1)
            path.pop()
        backtrack(0)


        return list(set(ans)^set(nums))[0]
            