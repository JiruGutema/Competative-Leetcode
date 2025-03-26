class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans, path = [], []

        def backtrack(n):
            if n == len(nums) and len(path) == len(nums):
                ans.append(path[:])
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

        for i in range(len(ans)):
            ans[i] = "".join(ans[i])


        return list(set(ans)^set(nums))[0]
            