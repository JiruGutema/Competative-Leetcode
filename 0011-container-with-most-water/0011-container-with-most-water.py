class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        maxArea = 0

        while i < j:
            area = min(height[j], height[i])*(j-i)
            maxArea = max(maxArea, area)
            if height[j] >height[i]:
                i += 1
            else:
                j -= 1
        return maxArea
