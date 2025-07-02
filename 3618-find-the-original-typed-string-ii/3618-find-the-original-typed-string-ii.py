class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        n = len(word)
        segs = [1]
        for i in range(1, n):
            if word[i] != word[i-1]:
                segs.append(1)
            else:
                segs[-1] += 1
        m = len(segs)

        less_than_k = 0
        if k >= m:
            dp = [1] + ([0] * (k-1))
            for i in range(1, m+1):
                prefix = [0] 
                for j in range(1, k):
                    prefix.append((prefix[j-1] + dp[j-1]) % 1000000007)
                dp = [0] * k
                for j in range(i, k):
                    dp[j] = (prefix[j] - prefix[j - min(segs[i-1], j)]) % 1000000007
            for j in range(m, k):
                less_than_k = (less_than_k + dp[j]) % 1000000007
        total = 1
        for v in segs:
            total = (total * v) % 1000000007
        return (total - less_than_k) % 1000000007