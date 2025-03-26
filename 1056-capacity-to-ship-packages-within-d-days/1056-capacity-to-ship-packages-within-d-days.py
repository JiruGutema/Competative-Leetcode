class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(capacity):
            day = 1
            curr = 0

            for i in weights:
                if curr + i > capacity:
                    day += 1
                    curr = 0
                curr += i
            return day <= days
            
        
        left = max(weights)  
        right = sum(weights)  

        while left <= right:
            mid = (left + right) // 2
            if possible(mid):  
                right = mid - 1  
            else:
                left = mid + 1  

        return left 