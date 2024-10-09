class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionaryOfNums = {}
        for i in range(len(nums)):
            if target-nums[i] in dictionaryOfNums:
                return [i, dictionaryOfNums[target-nums[i]]]
            dictionaryOfNums[nums[i]] = i

        