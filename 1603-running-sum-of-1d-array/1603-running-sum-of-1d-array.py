class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = []

        # curr = 0 
        for i in nums:
            # curr+=i
            # sums.append(curr)
            if not sums:
                sums.append(i)
            else:
                sums.append(sums[-1]+i)
        return sums