class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_points = sum(cardPoints)
        res = 0
        left = 0
        window = 0

        for r in range(len(cardPoints) - k):
            window += cardPoints[r]
        res = max(res, total_points-window)
        # print(window)
        for r in range(len(cardPoints)-k, len(cardPoints)):
            window = window - cardPoints[left] + cardPoints[r]
            
            res = max(res,total_points-window)
            left += 1
        return res