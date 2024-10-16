from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        
        # Count the frequency of each number
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        # Sort the hashmap by frequency and get the top k elements
        # Create a list of tuples (key, value) and sort by value in descending order
        sorted_items = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)
        
        # Extract the top k elements
        ans = [item[0] for item in sorted_items[:k]]
        
        return ans