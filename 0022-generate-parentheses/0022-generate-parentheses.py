class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        dp = [[] for _ in range(n+1)]
        dp[0] = [""]
        for i in range(1, n+1):
            for left in range(i):
                right = i - left - 1
                for l in dp[left]:
                    for r in dp[right]:
                        dp[i].append(("("+l+")"+r))
        return dp[n]

            




