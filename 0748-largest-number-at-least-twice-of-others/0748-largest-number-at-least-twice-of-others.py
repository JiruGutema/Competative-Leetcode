class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        sortedArray = sorted(nums)
        greater = sortedArray[-1]
        sortedArray[-1] = sortedArray[-1]/2


        if sortedArray[-1] >= sortedArray[-2]:
            return nums.index(greater)
        return -1
