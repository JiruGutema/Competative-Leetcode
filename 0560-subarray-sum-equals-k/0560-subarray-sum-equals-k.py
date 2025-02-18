from collections import Counter
class Solution:
    def subarraySum(self, nums, k):

        dictionary = Counter()
        nums = [0] + nums
        count = 0 

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        for i in range(len(nums)):
            curr_element = nums[i] - k
            
            if curr_element in dictionary.keys():
                count += dictionary[curr_element]
            dictionary[nums[i]] += 1
            
        return (count)