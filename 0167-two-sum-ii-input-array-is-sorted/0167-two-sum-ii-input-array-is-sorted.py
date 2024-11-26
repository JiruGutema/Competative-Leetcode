from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # brute force
        # n = len(numbers)
        # for i in range(n):
        #     for j in range(i, n):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]
        # time complexity O(n^2)
        # space complexity O(1)

        # efficient approach
        
        i = 0
        j = len(numbers) -1
        while j >= i:
            currentSum = numbers[i] + numbers[j]
            if currentSum == target:
                return [i+1, j+1]
            elif currentSum > target:
                j -= 1
            else:
                i += 1
        