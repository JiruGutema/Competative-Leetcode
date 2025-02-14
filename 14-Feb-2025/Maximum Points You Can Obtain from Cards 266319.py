# Problem: Maximum Points You Can Obtain from Cards - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        res = 0
        n = len(cardPoints)
        left , right = 0, 0
        for j in range(n-k,n):
            right += cardPoints[j]
        l,r = 0, n-k
        res = max(res, left + right)
        for i in range(1,k+1):
            left += cardPoints[l] 
            right -= cardPoints[r]
            l,r = l +1, r+1
            res = max(res,left+right)
        return res










        
        # total_points = sum(cardPoints)
        # res = 0
        # left = 0
        # window = 0

        # for r in range(len(cardPoints) - k):
        #     window += cardPoints[r]
        # res = max(res, total_points-window)
        
        # for r in range(len(cardPoints)-k, len(cardPoints)):
        #     window = window - cardPoints[left] + cardPoints[r]
            
        #     res = max(res,total_points-window)
        #     left += 1
        # return res