class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Create a dictionary to store the indices of each number
        num_indices = {}
        
        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            # If the number has been seen before
            if num in num_indices:
                # Check if the current index and the previous index are within k
                if abs(i - num_indices[num]) <= k:
                    return True
            # Update the index of the current number
            num_indices[num] = i
        
        # If no duplicates were found within k distance
        return False