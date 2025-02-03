class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        tracker = set()

        for nums in ranges:
            for num in range(nums[0], nums[1]+1):
                tracker.add(num)
        for i in range(left, right+1):
            if i not in tracker:
                return False
            
        return True
        