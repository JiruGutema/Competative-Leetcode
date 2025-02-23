from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_right = -1
        for i in range(n - 1, -1, -1):
            new_value = max_right 
            max_right = max(max_right, arr[i])
            arr[i] = new_value 

        return arr
