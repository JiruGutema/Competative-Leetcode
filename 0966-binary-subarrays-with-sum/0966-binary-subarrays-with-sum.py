class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        dictionary = Counter()
        nums = [0] + nums
        count = 0 

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        for i in range(len(nums)):
            curr_element = nums[i] - goal
            
            if curr_element in dictionary:
                count += dictionary[curr_element]
            dictionary[nums[i]] += 1
            
        return (count)