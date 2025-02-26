class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        idx_tracker = {}
        count = 0
        max_len = 0

        for i in range(len(nums)):
            current = nums[i]
            if current == 0:
                count -= 1
            else:
                count += 1

            if count == 0:
                max_len = i+1

            if count in idx_tracker:
                max_len = max(max_len, i-idx_tracker[count])
            else:
                idx_tracker[count] = i
        return max_len


        
        

