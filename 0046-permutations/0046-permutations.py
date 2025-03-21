class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        seen = set()
        
        def backtrack(idx):

            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in seen:
                    path.append(nums[i])
                    seen.add(nums[i])
                    backtrack(i+1)
                    path.pop()
                    seen.remove(nums[i])



        backtrack(0)

        return res


