class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        count = 0

        i = 0
        while i < k:
            selected = happiness[i]-i
            count += selected if selected > 0 else 0
            i += 1
        return count