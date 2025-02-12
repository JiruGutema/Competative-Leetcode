class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        count = 0
        times = 0
        n = len(piles)
        j = n-2

        while times*3 != n:
            count += piles[j]
            j -= 2
            times += 1
        return count

        