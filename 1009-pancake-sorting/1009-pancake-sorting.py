from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        
        def flip(k):
            start = 0
            while start < k:
                arr[start], arr[k] = arr[k], arr[start]
                start += 1
                k -= 1

        n = len(arr)
        for i in range(n - 1, -1, -1):
            # Find the index of the maximum element in arr[0..i]
            max_index = 0
            for j in range(1, i + 1):
                if arr[j] > arr[max_index]:
                    max_index = j
            
            # If the maximum element is not already in the correct place
            if max_index != i:
                # Flip the maximum number to the front if it's not already there
                if max_index != 0:
                    flip(max_index)
                    ans.append(max_index + 1)
                
                # Flip it to its correct position
                flip(i)
                ans.append(i + 1)

        return ans