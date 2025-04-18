class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ans = 0
        n = len(citations)
        citations.sort()

        for i in range(n):
            temp = min(citations[i], n-i)
            ans = max(temp, ans)
        return ans